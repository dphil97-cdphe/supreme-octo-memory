"""
https://acm-judge.urfu.ru/problem.aspx?space=1&num=1409

Two gangsters Harry and Larry had a rest at countryside. They decided to spend some time shooting, 
so they put several beer cans (no more than 10) on a log. Harry started to shoot cans one after 
another from the leftmost to the right and Larry – from the rightmost to the left. At some moment 
it happened so that they shot one and the same can.

Harry got indignant and claimed that Larry owed him a considerable sum of money because Larry 
deprived him of shooting some more cans. Larry became furious and told Harry that he owed even 
greater sum of money to Larry because of the same reason. They started to argufy but nobody 
remembered how many cans there were at the very beginning. And no one of them was going to 
search cans which was shot. Anyway, each of them remembered exactly how many cans he shot.

Determine how many cans were not shot by Harry and how many cans were not shot by Larry.

Input
-----
The only input line contains two integers — the number of cans shot by Harry and by Larry respectively.

Output
------
two integers — the number of cans that were not shot by Harry and the number 
of cans that were not shot by Larry, respectively.

Sample
------
input: 4 7
output: 6 3
"""
import sys

def process(tokens):

	cans_shot_by_harry = tokens[0]
	cans_shot_by_larry = tokens[1]

	total_cans = cans_shot_by_harry + cans_shot_by_larry - 1

	not_shot_by_harry = total_cans - cans_shot_by_harry

	not_shot_by_larry = total_cans - cans_shot_by_larry

	return not_shot_by_harry, not_shot_by_larry


def main():

	tokens = sys.stdin.read().split()

	result = process(tokens)

	print(result)

	return result


if __name__ == "__main__":
	main()