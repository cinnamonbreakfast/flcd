auto readConsole();
void print(auto);

int main() {
    int number;
    number = readConsole();

    if(number <= 2) {
        print("Number is prime");
        return;
    }

    for(int d = 3; d <= number/2; d++) {
        if(number%d == 0){
            print("Number not prime")
            return;
        }
    }

    print("Number is prime");

}