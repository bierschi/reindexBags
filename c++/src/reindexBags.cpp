//
// Created by christian on 06.07.18.
//
#include <iostream>
#include <string>


int main(int argc, char* argv[]){

    if (argc > 1 && argc < 4){

        if (argv[1] == std::string("-s")){

            std::string *sourceFolder = new std::string[sizeof(argv[2])];
            *sourceFolder = argv[2];
            std::cout << *sourceFolder;

        }

    } else {
        std::cerr << "wrong number of arguments!" << std::endl;
    }

    return 0;
}
