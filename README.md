Homework 3:

Report.
I found that everyone uses Chrome. However, considering I have been the only user to visit my website often, it seems natural for there to be a majority Chrome based user base. This point is particularly of interest with the way sessioning is done in that without persistent cookies, or other methods to store sessions beyond the length of the actual session, every visit will count as a completely new session despite the same users visiting the website. It highlights that the number of visitors on the site does not equate the number of users. Additionally this is a point that may affect other analytics such as screen dimensions and user interface designs. The average screen width to screen height ratio is skewed in favor of those who visit the site more often than others and it reveals a difficult design choice potentially if I were trying to make my website better responsive to users depending on their devices. It would make several factors more important like the total number of mobile users versus the total number of desktop users or the frequency of either of the users and if one metric is more important than the other one. The idea of trade-offs in developer decisions along with the  importance of complete data analysis to inform those decisions is my biggest take away from the analytics aspect of the course. 
Dashboard.

I decided to choose to report on the relative number of user agents visiting the website and the average screen width and screen height. I found that using a pie chart would be best for reporting on the number of user agents visiting the website. I thought that presenting this data in this manner would be the simplest and most decodable format with the intent of figuring out what portion of the total traffic is coming from what user agents. There exist other kinds of charts that may have been used, but I figured that if someone is trying to figure out what browers majority of their user base is using, it would be best to choose something a visual graphic demonstrating proportionally how the total number of users using each browser compares to one another. A bar chart would add a different metric like the total number of users of each browser, but that would introduce one more variable or one more concern like increasing traffic flow when the main goal was to make a comparison relative to each other. 

In regards to the average screen width and screen height I found that a bar chart is most practical. It outlines easily the dimensions of each and even without the exact measurements it is easy to decode the proportions of devices from the traffic flowing in. A pie chart might work to highlight the ratio between the two, however average measurements are the focus of the reporting metrics and therefore a bar chart remains more appropriate.

Homework 2:
Link: https://indominus.space/
Team Members: Jonathan Osorio
IP: 204.48.17.237
grader log information: 
  username: grader
  password: smmdkmtgrd3r

Homework 1:
Names of all members in your team:
  Jonathan Osorio
The password for user "grader" on your Apache server:
  smmdkmtgrd3r
Link to yourdomain.siteLinks to an external site., which has:

homepage with team member info and homework links
  https://indominus.space/
about pages for each team member
  https://indominus.space/members/osorio/index.html
  [robots.txt](https://indominus.space/robots.txt)
  [hw1/hello.php](https://indominus.space/hw1/hello.php)
  [hw1/report.html](https://indominus.space/hw1/report.html)
Details of Github auto deploy setup
  Essentially what I did was make a new github repo named indominus.space. I initialized my repo and uploaded the files from my remote ssh connection to the repo. Then I created a hook to detect push request so it may update to the IP address of the droplet and reflect the changes. I cloned my repo to my local machine, so now I'm able to edit from my local machine, and whenever I push something to the repo I'm able to then ssh to the server, git pull origin master, and the changes shortly appear afterwards on the site. 

  http://204.48.17.237:9000/hooks/deploy-indominus is my payload URL. I made a shell program to execute the following: 
    #!/bin/bash
    cd /var/www/indominus.space || exit
    git pull origin main
  Made it executable: chmod +x /var/www/indominus.space/deploy.sh
  Configured a webhooks file: hooks.json

  [
    {
      "id": "deploy-indominus",
      "execute-command": "/var/www/indominus.space/deploy.sh",
      "command-working-directory": "/var/www/indominus.space",
      "response-message": "Deploy script executed successfully"
    }
  ]

  Then started an event listener: webhook -hooks /home/osorio/hooks.json -port 9000

  So now I'm able to remotely work on the site. If I make any pushes, I ssh and git pull origin master.
    
Username/password info for logging into the site
  grader: password --- for https://reporting.indominus.space
Summary of changes to HTML file in DevTools after compression
  When gzip was implemented, it compressed the size for many of the files.
  	It included a different header too: 
  		content-encoding	gzip
  In the bottom left of the developer tools, there are two values displayed: transferred and resources. The amount of bytes transferred is now significantly lower compared to the number of bytes in the resources, which represent the uncompressed file sizes.
Summary of removing 'server' header
  I was able to a couple of changes to the header, but not many significant. I was able to display different amounts of information through changing ServerTokens and ServerSigniture. I tried using mod_headers and editing my configurations by including:
  	Header always set Server "CSE135 Server".
  However, for some reason the header never changed. I was able to include a custom header to prevent mime sniffing though, so I know mod_headers was working. I attempted to append or edit "CSE135 Server" to the Server header but it still did not change the value. I'm unsure to what occured.
