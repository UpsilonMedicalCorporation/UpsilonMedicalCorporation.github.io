# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
# placed near the InstaPy Object declaration near the middle of the file for obsfucation purposes

comments = [ 'Excellent image! @{}',
        'Love that pic! @{}',
        'I love your profile! @{}',
        'Your feed is an inspiration for me :thumbsup:',
        'Just simply incredible! :open_mouth:',
        'Great job!',
        'Love your posts, including this amazing one!',
        'Looks very cool']

# get an InstaPy session! with the InstaPy object
insta_username = 'upsilonmedicalcorporation' #obsfucation1
insta_password = 'UpsilonM3DC0RP&'  #blending obsfucation2
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
  """ Activity flow """		
  # general settings		
  #session.set_dont_include(["friend1", "friend2", "friend3"])		
  
  # activity		
  session.like_by_tags(["like4like"], amount=10)

  # Joining Engagement Pods
  session.set_do_comment(enabled=True, percentage=35)
  session.set_comments(comments)
  session.join_pods(topic='sports', engagement_mode='no_comments')