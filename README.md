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
