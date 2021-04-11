class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        m = len(mat)
        if m > 0:
            n = len(mat[0])
        else:
            n = 0

        ans = []
        total = 0
        for i in range(m):
            ans.append([])
            for j in range(n):
                # no. of 1 submatrices start with i,j
                curr_cell_count = 0
                cmax = n

                for k in range(i, m):
                    if mat[k][j] == 0:
                        break
                    l = j
                    while l < cmax:
                        if mat[k][l]:
                            l += 1
                            curr_cell_count += 1
                            total += 1

                        else:
                            cmax = l
                            break

                ans[i].append(curr_cell_count)
        print(ans)
        return total
