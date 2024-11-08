""""

Problem Description
--------------------
It’s restless now on the slips of the intergalactic port’s sixth dock of planet of Torn. 
No longer then in a month the reconstruction of the small ironclad corvette “Eniya” will be finished. 
And again this battle ship and its brave team would have to struggle for the control over 
plutonium mines of Sibelius. The work cannot be stopped even for a second, self-powered laser welders 
work round the clock. Joints of robots-repairers fuse because of this permanent work. Nevertheless,
they can’t stop not for a single moment. Now in all this turmoil it is discovered that corvette’s 
thermopanels again need an urgent processing with thorium sulphide. It is known that the processing 
of the one square meter of the panel needs 1 nanogramm of sulphide. In general, it is needed to 
process N rectangular panels, which dimensions are A by B meters. It is necessary to calculate 
as fast as possible, how much sulphide is needed in general for the processing of all panels of 
“Eniya”. Moreover, do not forget, that the panels need processing of both sides.

Input
------
The only line contains integers N (1 ≤ N ≤ 100), A (1 ≤ A ≤ 100), B (1 ≤ B ≤ 100).

Output
------
Output the weight of thorium sulphide in nanogramms needed for the processing.

Sample
-----
input: 5 2 3 output: 60

Strategy
--------
calculate (N)(A)(B)(2)

Run (powershell)
----------------
@"
5 2 3
"@ | python 1293_eniya.py

"""
import sys


def process(tokens):
    
    token_ints = [int(x) for x in tokens]

    result = 1

    for token_int in token_ints:
        result *= token_int
    
    # Multiply by 2 to account for both sides of panel
    return result * 2

def main():
     
    tokens = sys.stdin.read().split()

    result = process(tokens)

    print(result)

    return result

if __name__ == "__main__":
    main()
  

