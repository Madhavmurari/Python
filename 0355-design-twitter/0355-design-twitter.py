class Twitter:

    def __init__(self):
        self.count=0
        self.tweetmap=defaultdict(list)
        self.followmap=defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count,tweetId])
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        maxheap=[]
        self.followmap[userId].add(userId)
        for followeeId in self.followmap[userId]:
            if followeeId in self.tweetmap:
                index=len(self.tweetmap[followeeId])-1
                count,tweetId=self.tweetmap[followeeId][index]
                maxheap.append([count,tweetId,followeeId,index-1])
        heapq.heapify(maxheap)
        while maxheap and len(res)<10:
            count,tweetId,followeeId,index=heapq.heappop(maxheap)
            res.append(tweetId)
            if index>=0:
                count,tweetId=self.tweetmap[followeeId][index]
                heapq.heappush(maxheap,[count,tweetId,followeeId,index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
        



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)