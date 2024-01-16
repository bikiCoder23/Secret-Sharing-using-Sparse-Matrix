# Secret-Sharing-using-Sparse-Matrix
This is an implementation of a secure mode of data (in bits) transmission using sparse matrix under the field of Information Security, my project for Summer Research Internship program at Jadavpur University under **Dr. Bibhas Chandra Dhara**.

## Procedure
To try my algorithm, clone the python file *secret_sharing.py* follow the steps sequentially:
1. Open the file with any python friendly code editor for example vscode, pycharm, jupyter notebook, etc.
2. Install all the mentioned libraries if not already and compile the code.
3. After successfully compiling the code, it will ask for a input string consisting n data bits in binary format. Enter the input accordingly.
4. As a result the algorithm will generate the corresponding chromatic polynomial of the binary string provided as the input.
5. The program will then equate the polynomial for x= r, r+1, r+2...,n+r and provide the corresponding values in the form of an array,
   where r is any randomly selected integer,
         n is the length of the input binary string and can be of any possible length.
6. These equated values can be shared to reciever using any kind of unsecured channel since this data can't be interpreted by the attacker/hacker.
7. The sender will have to send the key which consists of only a single number, i.e, r to the reciever via secured channel, so that the reciever will have the key pair of (n, r).
8. The reciever will subsequently generate a series from `r` to `n+r` and feed the number series along with the recieved values to a Lagrange Interpolation Calculator for example, [AtoZmath](https://atozmath.com/CONM/NumeInterPola.aspx?q=LI), to re-generate the chromatic polynomial.
9. Now take the coefficient of the chromatic polynomial and enter it into the program such that it will regenerate input binary string/original message from the sender in the reciever's end.

*Any Feedback is much appreciated!!*

### Contact Me
[Mail](bikramjit2001vibgyor@gmail.com)                                                                                                                      
[LinkedIn](www.linkedin.com/in/bikramjit-saha-569a8720a)
