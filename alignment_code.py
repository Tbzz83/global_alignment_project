def game_board(t, q, match_score=1, mismatch_penalty=0):
    res = []
    row = []
    for i in range(len(t) + 1):
        row.append(0)
    res.append(row)

    for i in range(len(q)):
        row = []
        row.append(0)
        for j in range(len(t)):
            if t[j] == q[i]:
                row.append(match_score)
            else:
                row.append(mismatch_penalty)
        res.append(row)

    return res
# j is for q, i is for tSs
# q is top row, t is columns
def dynamic_table(t, q, game_board, gap_penalty=0):
    t_path = []

    # first row
    for j, rows in enumerate(game_board):
        path = []
        for i, cols in enumerate(rows):
            left_val = game_board[j][i - 1] if i > 0 else None
            above_val = game_board[j - 1][i] if j > 0 else None
            diagonal_val = game_board[j - 1][i - 1] if j > 0 and i > 0 else None

            if left_val is not None and above_val is not None and diagonal_val is not None:
                l = left_val + gap_penalty
                a = above_val + gap_penalty
                d = diagonal_val + game_board[j][i]
                if l > a and l > d:
                    game_board[j][i] = l
                    path.append('r')
                elif a > l and a > d:
                    game_board[j][i] = a
                    path.append('d')
                elif d > l and d > a:
                    game_board[j][i] = d
                    path.append('diag')
                elif l == a and l == d:
                    game_board[j][i] = l
                    path.append(['r', 'd', 'diag'])
                elif l == a:
                    game_board[j][i] = l
                    path.append(['r', 'd'])
                elif a == d:
                    game_board[j][i] = a
                    path.append(['d', 'diag'])
                elif l == d:
                    game_board[j][i] = l
                    path.append(['r', 'diag'])
                else:
                    game_board[j][i] = 0
                    path.append(0)



            elif left_val is not None and above_val is not None:
                l = left_val + gap_penalty
                a = above_val + gap_penalty
                if l > a:
                    game_board[j][i] = l
                    path.append('r')
                if l == a:
                    game_board[j][i] = l
                    path.append(['r', 'd'])
                else:
                    game_board[j][i] = a
                    path.append('d')

            elif left_val is not None and diagonal_val is not None:
                l = left_val + gap_penalty
                d = diagonal_val + game_board[j][i]
                if l > d:
                    game_board[j][i] = l
                    path.append('r')
                elif l == d:
                    game_board[j][i] = l
                    path.append(['r', 'diag'])
                else:
                    game_board[j][i] = d
                    path.append('diag')

            elif above_val is not None and diagonal_val is not None:
                a = above_val + gap_penalty
                d = diagonal_val + game_board[j][i]
                if a > d:
                    game_board[j][i] = a
                    path.append('d')
                elif a == d:
                    game_board[j][i] = a
                    path.append(['d', 'diag'])
                else:
                    game_board[j][i] = d
                    path.append('diag)')
            elif left_val is not None:
                l = left_val + gap_penalty
                game_board[j][i] = l
                path.append('r')
            elif above_val is not None:
                a = above_val + gap_penalty
                game_board[j][i] = a
                path.append('d')
            else:
                game_board[j][i] = 0
                path.append(0)


        t_path.append(path)

    return game_board, t_path

def align(t, q, path, row_idx=-1, col_idx=-1, x='', y='', alignments=[]):
    # q, x = row
    # t, y = col
    if path[row_idx][col_idx] == 0:
        alignments.append([x,y])
        print([x,y])
        return alignments

    if path[row_idx][col_idx] == 'r':
        align(t,q,path,row_idx,col_idx-1, '-' + x, t[col_idx] + y, alignments)

    elif path[row_idx][col_idx] == 'd':
        align(t,q,path,row_idx-1, col_idx, q[row_idx] + x, '-' + y, alignments)

    elif path[row_idx][col_idx] == 'diag':
        align(t,q,path,row_idx-1,col_idx-1, q[row_idx] + x, t[col_idx] + y, alignments)

    elif type(path[row_idx][col_idx]) == list:
        for option in path[row_idx][col_idx]:
            if option == 'r':
                align(t,q,path,row_idx,col_idx-1, '-' + x, t[col_idx] + y, alignments)

            if option == 'd':
                align(t,q,path,row_idx-1, col_idx, q[row_idx] + x, '-' + y, alignments)

            if option == 'diag':
                align(t,q,path,row_idx-1,col_idx-1, q[row_idx] + x, t[col_idx] + y, alignments)

    return alignments

def main(t,q,match_score=1,mismatch_penalty=0,gap_penalty=0):
    # By default, match_score = 1, mismatch_penalty = 0, gap_penalty = 0
    # Enter match_score and mismatch_penalty in game_board()
    g_board = game_board(t, q, match_score = match_score, mismatch_penalty=mismatch_penalty)

    # Enter gap_penalty in dynamic_table()
    d_table, path = dynamic_table(t, q, g_board, gap_penalty=gap_penalty)

    print(len(path))
    print(len(path[0]))

    alignments = align(t, q, path)
    # print(alignment)
    return alignments, d_table, path

# Enter in target (t) and query (q) strings here
#t = 'GNPKVK'
#q = 'GSAPVK'

# Example sequence
t = 'AAATTGAAGAGTTTGATCATGGCTCAGATTGAACGCTGGCGGCAGGCCTAACACATGCAA'
q = 'GTCGACAGAGTTCGATCCTGGCTCAGGACGAACGCTGGCGGCGTGCCTAATACATGCAAG'

#with open(t, 'r') as file:
    # Read all lines from the file
#    lines = file.readlines()

    # Concatenate lines from the second line onwards into one string
#    t = ''.join(lines[1:]).replace('\n', '')

#with open(q, 'r') as file:
    # Read all lines from the file
#    lines = file.readlines()

    # Concatenate lines from the second line onwards into one string
#    q = ''.join(lines[1:]).replace('\n', '')

import sys
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())



# Change scoring here
match_score = 1
mismatch_score = -1
gap_score = -2

alignments, d_table, path = main(t,q,match_score,mismatch_score,gap_score)


#for item in alignments:
#    print(item[1])
#    print(item[0])
 #   print('---')

#print(f'The number of unique alignments is {len(alignments)}')

#for row in d_table:
    #print(row)
# --------------------------------------------------------
# Below is the code for the test_alignment
from Bio import Align


aligner = Align.PairwiseAligner()
aligner.mode = 'global'
aligner.match_score = match_score
aligner.mismatch_score = mismatch_score
aligner.gap_score = gap_score
test_alignments = aligner.align(t,q)

#for i in range(0,len(alignments)):
    #print(alignments[i])
    #print(test_alignments[i])



def cross_check(alignments, test_alignments):
   res = False
   for i in test_alignments:
       val = [i[1],i[0]]
       if val in alignments:
           res = True
           continue
       else:
           res = False
           return res
   return res

res = cross_check(alignments,test_alignments)
if res == True:
   print('All alignments match')
   print(f'The number of unique alignments is {len(alignments)}')
else:
   print('Alignments do not match')

    