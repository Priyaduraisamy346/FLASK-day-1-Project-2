#import flask
from flask import Flask
app=Flask(__name__)
@app.route('/')
def Moral_Story  ():
    return "<div style='background:grey'><center><h1> The Golden Egg</center></h1><br><p>Once upon a time, a farmer had a goose that laid a golden egg every day. The farmer used to sell that egg and earn enough money to meet their family's day-to-day needs. One day, the farmer thought that if he could get more such golden eggs and make a lot of money and become a wealthy person. The farmer decided to cut the goose and remove all the golden eggs from its stomach. As soon as they killed the bird and opened the goose’s stomach, they found no eggs. The foolish farmer realized they had destroyed their last resource out of greed.<br><br><b>Moral:</b> Greed destroys your resource.<br><br></hr></p></div>"
if __name__=='__main__':
   app.run(debug=True)    
