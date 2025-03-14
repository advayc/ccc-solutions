#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
 
const ll INF = 1e18; // for second min in segtree (a very large number)
const ll NEG_INF = -1000000000000000000LL; // negative infinity for candidate segtree
 
// ----- SEGMENT TREE FOR MINIMUM (on best values) -----
struct NodeMin {
    ll minVal;
    ll secondMin;
    int idx; // index where minVal occurs
};
 
// Combine function: given two nodes, compute the node for their union.
NodeMin combineMin(const NodeMin &a, const NodeMin &b) {
    NodeMin res;
    if(a.minVal < b.minVal){
        res.minVal = a.minVal;
        res.idx = a.idx;
        res.secondMin = min(a.secondMin, b.minVal);
    } else if(a.minVal > b.minVal){
        res.minVal = b.minVal;
        res.idx = b.idx;
        res.secondMin = min(a.minVal, b.secondMin);
    } else { // equal
        res.minVal = a.minVal;
        res.idx = a.idx; // arbitrary pick
        res.secondMin = min(a.secondMin, b.secondMin);
        if(res.secondMin == INF) res.secondMin = res.minVal; // if duplicate exists
    }
    return res;
}
 
struct SegTreeMin {
    int size;
    vector<NodeMin> tree;
 
    SegTreeMin(int n) {
        size = n;
        tree.resize(4 * n);
    }
 
    void build(vector<ll> &arr) { // arr is 1-indexed of length size
        build(1, 1, size, arr);
    }
 
    void build(int idx, int l, int r, vector<ll> &arr) {
        if(l == r) {
            tree[idx].minVal = arr[l];
            tree[idx].secondMin = INF;
            tree[idx].idx = l;
            return;
        }
        int mid = (l + r) / 2;
        build(idx*2, l, mid, arr);
        build(idx*2+1, mid+1, r, arr);
        tree[idx] = combineMin(tree[idx*2], tree[idx*2+1]);
    }
 
    void update(int pos, ll val) {
        update(1, 1, size, pos, val);
    }
 
    void update(int idx, int l, int r, int pos, ll val) {
        if(l == r) {
            tree[idx].minVal = val;
            tree[idx].secondMin = INF;
            tree[idx].idx = pos;
            return;
        }
        int mid = (l + r) / 2;
        if(pos <= mid) update(idx*2, l, mid, pos, val);
        else update(idx*2+1, mid+1, r, pos, val);
        tree[idx] = combineMin(tree[idx*2], tree[idx*2+1]);
    }
 
    NodeMin query(int ql, int qr) {
        return query(1, 1, size, ql, qr);
    }
 
    NodeMin query(int idx, int l, int r, int ql, int qr) {
        if(ql > r || qr < l) {
            NodeMin dummy;
            dummy.minVal = INF;
            dummy.secondMin = INF;
            dummy.idx = -1;
            return dummy;
        }
        if(ql <= l && r <= qr)
            return tree[idx];
        int mid = (l + r) / 2;
        NodeMin leftNode = query(idx*2, l, mid, ql, qr);
        NodeMin rightNode = query(idx*2+1, mid+1, r, ql, qr);
        return combineMin(leftNode, rightNode);
    }
};
 
// ----- SEGMENT TREE FOR MAXIMUM (on candidate values) -----
struct NodeMax {
    ll maxVal;
    int idx;
};
 
struct SegTreeMax {
    int size;
    vector<NodeMax> tree;
 
    SegTreeMax(int n) {
        size = n;
        tree.resize(4 * n);
    }
 
    void build(vector<ll> &arr) { // arr is 1-indexed
        build(1, 1, size, arr);
    }
 
    void build(int idx, int l, int r, vector<ll> &arr) {
        if(l == r) {
            tree[idx].maxVal = arr[l];
            tree[idx].idx = l;
            return;
        }
        int mid = (l + r) / 2;
        build(idx*2, l, mid, arr);
        build(idx*2+1, mid+1, r, arr);
        if(tree[idx*2].maxVal >= tree[idx*2+1].maxVal)
            tree[idx] = tree[idx*2];
        else
            tree[idx] = tree[idx*2+1];
    }
 
    void update(int pos, ll val) {
        update(1, 1, size, pos, val);
    }
 
    void update(int idx, int l, int r, int pos, ll val) {
        if(l == r) {
            tree[idx].maxVal = val;
            tree[idx].idx = pos;
            return;
        }
        int mid = (l + r) / 2;
        if(pos <= mid)
            update(idx*2, l, mid, pos, val);
        else
            update(idx*2+1, mid+1, r, pos, val);
        if(tree[idx*2].maxVal >= tree[idx*2+1].maxVal)
            tree[idx] = tree[idx*2];
        else
            tree[idx] = tree[idx*2+1];
    }
 
    NodeMax query(int ql, int qr) {
        return query(1, 1, size, ql, qr);
    }
 
    NodeMax query(int idx, int l, int r, int ql, int qr) {
        if(ql > r || qr < l) {
            NodeMax dummy;
            dummy.maxVal = NEG_INF;
            dummy.idx = -1;
            return dummy;
        }
        if(ql <= l && r <= qr)
            return tree[idx];
        int mid = (l + r) / 2;
        NodeMax leftNode = query(idx*2, l, mid, ql, qr);
        NodeMax rightNode = query(idx*2+1, mid+1, r, ql, qr);
        if(leftNode.maxVal >= rightNode.maxVal)
            return leftNode;
        else
            return rightNode;
    }
};
 
// ----- MAIN SOLUTION -----
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N, M, Q;
    cin >> N >> M >> Q;
    vector<int> penColor(N+1);
    vector<ll> penVal(N+1);
    // For each colour (1-indexed), use a map: prettiness -> frequency.
    vector<map<ll,int>> colorMap(M+1);
 
    for (int i = 1; i <= N; i++){
        int c; ll p;
        cin >> c >> p;
        penColor[i] = c;
        penVal[i] = p;
        colorMap[c][p]++;
    }
 
    // For each colour compute:
    //   best[c] = maximum prettiness among pens of colour c.
    //   candidate[c] = if there is more than one pen with best value, then best[c] (pen not used in base selection)
    //                  otherwise, the second highest prettiness.
    vector<ll> best(M+1, 0), candidate(M+1, NEG_INF);
    ll baseSum = 0;
    for (int c = 1; c <= M; c++){
        auto it = colorMap[c].rbegin();
        best[c] = it->first;
        baseSum += best[c];
        if(it->second > 1)
            candidate[c] = best[c];
        else {
            auto it2 = it; it2++;
            if(it2 != colorMap[c].rend())
                candidate[c] = it2->first;
            else
                candidate[c] = NEG_INF;
        }
    }
 
    // Build segment trees.
    vector<ll> bestArr(M+1), candArr(M+1);
    for (int c = 1; c <= M; c++){
        bestArr[c] = best[c];
        candArr[c] = candidate[c];
    }
    SegTreeMin segMin(M);
    segMin.build(bestArr);
    SegTreeMax segMax(M);
    segMax.build(candArr);
 
    // A lambda to compute the answer given the current state.
    auto computeAnswer = [&]() -> ll {
        // Query segMin to get global minimum among best[c]
        NodeMin globalMinNode = segMin.query(1, M);
        ll globalMin = globalMinNode.minVal;
        int argmin = globalMinNode.idx;
        ll globalMin2 = globalMinNode.secondMin;
        if(globalMin2 == INF) globalMin2 = globalMin; // if duplicate exists
        // Option 1: using candidate from the argmin colour.
        ll option1 = candidate[argmin] - globalMin2;
        // Option 2: best candidate from colours other than argmin.
        ll otherMax = NEG_INF;
        if(argmin > 1){
            NodeMax leftQuery = segMax.query(1, argmin-1);
            otherMax = max(otherMax, leftQuery.maxVal);
        }
        if(argmin < M){
            NodeMax rightQuery = segMax.query(argmin+1, M);
            otherMax = max(otherMax, rightQuery.maxVal);
        }
        ll option2 = otherMax - globalMin;
 
        ll bestGain = max(option1, option2);
        if(bestGain < 0) bestGain = 0;
        return baseSum + bestGain;
    };
 
    // Print answer for initial state.
    cout << computeAnswer() << "\n";
 
    // Process Q queries.
    for (int qi = 0; qi < Q; qi++){
        int t, i;
        cin >> t >> i;
        if(t == 1){
            // Change the colour of pen i.
            int newColor; 
            cin >> newColor;
            int oldColor = penColor[i];
            ll p = penVal[i];
            if(oldColor == newColor){
                cout << computeAnswer() << "\n";
                continue;
            }
            // Remove pen i from its old colour.
            {
                auto &mp = colorMap[oldColor];
                mp[p]--;
                if(mp[p] == 0) mp.erase(p);
            }
            // Insert pen i into the new colour.
            {
                auto &mp = colorMap[newColor];
                mp[p]++;
            }
            penColor[i] = newColor;
 
            // Update oldColor group.
            {
                ll oldBest = best[oldColor];
                auto &mp = colorMap[oldColor];
                auto it = mp.rbegin();
                best[oldColor] = it->first;
                if(it->second > 1)
                    candidate[oldColor] = best[oldColor];
                else {
                    auto it2 = it; it2++;
                    if(it2 != mp.rend())
                        candidate[oldColor] = it2->first;
                    else
                        candidate[oldColor] = NEG_INF;
                }
                baseSum += (best[oldColor] - oldBest);
                segMin.update(oldColor, best[oldColor]);
                segMax.update(oldColor, candidate[oldColor]);
            }
 
            // Update newColor group.
            {
                ll oldBest = best[newColor];
                auto &mp = colorMap[newColor];
                auto it = mp.rbegin();
                best[newColor] = it->first;
                if(it->second > 1)
                    candidate[newColor] = best[newColor];
                else {
                    auto it2 = it; it2++;
                    if(it2 != mp.rend())
                        candidate[newColor] = it2->first;
                    else
                        candidate[newColor] = NEG_INF;
                }
                baseSum += (best[newColor] - oldBest);
                segMin.update(newColor, best[newColor]);
                segMax.update(newColor, candidate[newColor]);
            }
 
        } else if(t == 2){
            // Change the prettiness of pen i.
            ll newVal; 
            cin >> newVal;
            int c = penColor[i];
            ll oldVal = penVal[i];
            {
                auto &mp = colorMap[c];
                mp[oldVal]--;
                if(mp[oldVal] == 0) mp.erase(oldVal);
                mp[newVal]++;
            }
            penVal[i] = newVal;
 
            {
                ll oldBest = best[c];
                auto &mp = colorMap[c];
                auto it = mp.rbegin();
                best[c] = it->first;
                if(it->second > 1)
                    candidate[c] = best[c];
                else {
                    auto it2 = it; it2++;
                    if(it2 != mp.rend())
                        candidate[c] = it2->first;
                    else
                        candidate[c] = NEG_INF;
                }
                baseSum += (best[c] - oldBest);
                segMin.update(c, best[c]);
                segMax.update(c, candidate[c]);
            }
        }
        cout << computeAnswer() << "\n";
    }
 
    return 0;
}
