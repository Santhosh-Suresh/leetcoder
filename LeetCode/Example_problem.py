from functools import reduce

class Solution( object ):
    def canFormArray(self , arr , pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        # Check if all elements are repeated once
        arr_set = set( arr )
        set_pieces = {val for piece in pieces for val in piece}
        if arr_set != set_pieces:
            return False

        # Convert into string and check for pattern repetition
        arr_string = self.list_to_string( arr )

        for piece in pieces:
            piece_str = self.list_to_string( piece )
            if arr_string.find( piece_str ) == -1:
                return False
            arr_string.replace( piece_str, "", 1 )

        return True

    def list_to_string(self , l):

        if type(l) == list:
            if len(l) == 1:
                return str(l[0])
            return reduce( lambda x , y: str( x ) + str( y ) , l )
        return str(l)