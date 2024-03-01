#include <iostream>

int main() {
    
    // integer and whole number
    int age = 21;
    int year = 2023;
    int days = 7.5;

    // double (numbers with decimals)
    double gpa = 2.5;
    double price = 10.99;
    double temp = 25.1;

    // single character
    char grade = 'A';
    char inital = 'B';
    char currency = '$';

    // boolean 
    bool student = false;
    bool power = true;
    bool forSale = true;

    //strings
    std::string name = "Advay"; //double quotes 
    std::string Date = "Sunday";
    std::string food = "Pizza";
    std::string address = "123 Real Street";

    std::cout << "Hello " << name << '\n';
    std::cout << "I see that you are " << age << " years old" << std::endl;

    //practice
    int friend_age = 20;
    double money = 44.44;
    char symbol = '%';
    std::string friend_name = "joe";

    std::cout << "Hello " << name << "!. I see you are with " << friend_name << ", have a good time together!" <<'\n';
    std::cout << "I see you are " << age << " years old and your friend is " << friend_age << " years old!" <<'\n';


    return 0;
}

/*
    int x = 5; //declaration
    int y = 6;
    int sum = x+y
    
    std::cout << x << '\n';
    std::cout << y << '\n';
    std::cout << sum << '\n';
    */