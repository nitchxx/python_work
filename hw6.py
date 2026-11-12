blog_views = [150, 800, 2500, 600, 1200, 450, 3000]
total_no_of_views = 0
trending_posts = 0

for views in blog_views :
    if views > 1000 :
        print(views ,"views : Trending")
    elif views >= 500 and views <= 1000 :
        print(views ,"views : Average")
    else :
        print(views," views : Low Traffic")

for total_views in blog_views :
    total_no_of_views += total_views
print("Total views : ",total_no_of_views)

for trending_views in blog_views :
    if trending_views > 1000 :
        trending_posts += 1

print("Trending Posts : ",trending_posts)