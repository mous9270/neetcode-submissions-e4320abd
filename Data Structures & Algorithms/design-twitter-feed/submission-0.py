class Twitter:

    def __init__(self):
      self.posts=defaultdict(list)
      self.follows=defaultdict(set)
      self.count=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
      self.posts[userId].append((tweetId,self.count))
      self.count+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
      p=self.posts[userId][-10:]
      for i in self.follows[userId]:
        p.extend(self.posts[i][-10:])
      sp=sorted(p,key=lambda i:i[1], reverse=True)
      ans=[]
      for i in sp:
        if len(ans)<10:
          ans.append(i[0])
      return ans
        

    def follow(self, followerId: int, followeeId: int) -> None:
      self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
      self.follows[followerId].discard(followeeId)
