# Take-Home-Engineering-Challenge
Take-Home-Engineering-Challenge

<h1>The Problem</h1>

Getting around large cities can be quite a hassle, and New York City is no exception. One thing that helps, is being able to predict how long a trip might take and how much that trip might cost. Luckily, NYC provides public data about transportation which includes all of the metrics we need!

Your assignment, is to help us quickly look at transportation fare data for tips between different boroughs in NYC so that when we travel there, it is easier for us to get around.

This is a freeform assignment. You can write a web API that returns a set of trip metrics. You can write a web frontend that visualizes the trips and shows cheapest/fastest options. We also spend a lot of time in the shell, so a CLI that gives us a few options would be great. And don't be constrained by these ideas if you have a better one!

The only requirements for the assignment are:

<ol>
  <li>We can filter based on yellow cab, green cab, and for-hire vehicle.</li>
<li>We can provide a start and end borough for our trip.</li>
<li>We can filter based on datetime.</li>
<li>The returned data shows some interesting metrics that will help us get around.</li>
<li>Your code is well-tested.</li>
<li>Documentation is provided for how to build and run your code.</li>
</ol>

Feel free to tackle this problem in a way that demonstrates your expertise of an area -- or takes you out of your comfort zone. For example, if you build Web APIs by day and want to build a frontend to the problem or a completely different language instead, by all means go for it - learning is a core competency in our group. Let us know this context in your solution's documentation.

New York City transportation data is located <a href='https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page'>here</a>. A copy of the <a href='https://cseboulderinterview.blob.core.windows.net/triprecord/tripdata.zip'>Jan 2018 data</a> as well is located here.

<h1>Instructions:</h1>
<ol>
  <li>Clone the repo</li>
  <li>Download data files and extract them into the application folder</li>
  <li>Run the application</li>
 </ol>
  
  <h1>Thinking Out Loud</h1>
  
  <h2>Rationale Behind Technical Choice</h2>
  When I first saw the large data files I immediately thought of Python. Due to the time constraint with Python along with a few modules, I could get something working quickly.
  
  <h2>Trade-Offs</h2>
  I knew using Python that the application wouldn't be scalable and the most performant. I just wanted to get a proof of concept working in the time constraint.
  
  <h2>If I Had More Time</h2>
  I would definitely look into making this more scalable and efficient. There has to be a way this can run in Azure. I only made it work with Jan 2018 data. What about other months? Create web apis to get the data
  I was not able to make the data filterable by datatime. I would make that work. 
  
  So better UI, scalable and fast data analysis. I think the answer to all my wants exist somewhere in Azure, I just needed more time.
  
 
