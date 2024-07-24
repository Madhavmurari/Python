class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        mapp=Counter(hand)

        # Step 3: Sort the unique card values
        sorted_key=sorted(mapp.keys()) 

        # Step 4: Form consecutive groups
        for key in sorted_key:
            if mapp[key]>0:   # If this card is still available
                start_count=mapp[key]
                # Check and form a group starting from `key`
                for i in range(key,key+groupSize):
                    if mapp[i]<start_count:
                        return False
                    mapp[i]-=start_count
        return True   #Return True if all groups are formed successfully

