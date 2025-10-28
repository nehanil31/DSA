class Solution:
    def searchnext(self,board,word,m,n,k,row,col)->bool:
        if k==len(word):
            return True
        if m<0 or n<0 or m==row or n==col or board[m][n]!=word[k] or board[m][n]=='!':
            return False
        c=board[m][n]
        board[m][n]='!' 
        top=self.searchnext(board,word,m-1,n,k+1,row,col)
        bottom=self.searchnext(board,word,m+1,n,k+1,row,col)
        left=self.searchnext(board,word,m,n-1,k+1,row,col)
        right=self.searchnext(board,word,m,n+1,k+1,row,col)
        board[m][n]=c 
        return top or bottom or left or right      

    def exist(self, board: List[List[str]], word: str) -> bool:
        k=0
        row=len(board)
        col=len(board[0])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[k]:
                    if self.searchnext(board,word,i,j,k,row,col):
                        return True
        return False                

                        
                

        
