# BAT8-Logisim-Computer
A functional computer created in the logic-simulation program Logisim, complete with an assembler written in python

I don't plan on updating this or adding any more features, this is mostly being uploaded for educational purposes.

I've included a python script that I used as an assembler. It takes instructions written in an assembly language specific to the machine, and outputs a binary file containing the machine code that BAT8 accepts. In order to run this machine code, I used a hex editor to open the compiled binary file, copied the contents, and pasted them into BAT8's program ROM module (located in the top right of the circuit).

Keep in mind that the machine contains two ROM modules: one located in the top right of the circuit (program ROM) and one located on the right. The one on the right contains BAT8's microcode, which defines which instructions do what. A copy of this microcode is also included in this repository, but it was hand written into a hex editor by me, so there isn't any source code I can provide.

I have also included a few sample programs I wrote, and I will try to document the exact instruction set in the future.
