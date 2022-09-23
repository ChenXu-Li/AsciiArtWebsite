#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import execute_img
import cgi, os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['filename']

text_img="qweasdzxc"

# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open('tmp/' + fn, 'wb').write(fileitem.file.read())
   #open('D:\\justplay\\asciiweb\\www\\tmp\\' + fn, 'wb').write(fileitem.file.read())

   message = 'The file "' + fn + '" was uploaded successfully'
   text_img = execute_img.exe_img('tmp/' + fn)
else:
   message = 'No file was uploaded'
print('Content-type:text/html \n\n')#\n\n很重要
# print(

# '''
# <!DOCTYPE html>
# <html>
#     <head>
#         <meta charset=\"utf-8\">
#         <title>img</title>
#     </head>
#     <body>
#         <p>{0}</p>     
#         <p>{1}</p>  
        
#         <textarea name="description">{2}</textarea>
    
#         <tt style="line-height:0;background-color: pink;"></tt>
   
#     </body>
# </html>
#     '''.format(message,fn,text_img)
# )
print(

'''


<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>ASCII art</title>


<meta name="viewport" content="width=device-width, initial-scale=1">



<style>


/*----------------按钮-----------------*/
@import url('https://fonts.googleapis.com/css2?family=Raleway:wght@400;700&display=swap');
*{
    margin: 0;
    padding: 0;
    border:0;
    box-sizing: border-box;
}

a{
    position: relative;
    display: inline-block;
    padding: 25px 30px;
    margin: 30px 95px;
    color: #03e9f4;
    text-decoration: none;
    text-transform: uppercase;
    transition: 0.5s;
    letter-spacing: 4px;
    overflow: hidden;
    margin-right: 50px;
   
}
a:hover{
    background: #03e9f4;
    color: #050801;
    box-shadow: 0 0 5px #03e9f4,
                0 0 25px #03e9f4,
                0 0 50px #03e9f4,
                0 0 200px #03e9f4;
     -webkit-box-reflect:below 1px linear-gradient(transparent, #0005);
}
a:nth-child(1){
    filter: hue-rotate(270deg);
}
a:nth-child(2){
    filter: hue-rotate(110deg);
}
a span{
    position: absolute;
    display: block;
}
a span:nth-child(1){
    top: 0;
    left: 0;
    width: 100%;
    height: 2px;
    background: linear-gradient(90deg,transparent,#03e9f4);
    animation: animate1 1s linear infinite;
}
@keyframes animate1{
    0%{
        left: -100%;
    }
    50%,100%{
        left: 100%;
    }
}
a span:nth-child(2){
    top: -100%;
    right: 0;
    width: 2px;
    height: 100%;
    background: linear-gradient(180deg,transparent,#03e9f4);
    animation: animate2 1s linear infinite;
    animation-delay: 0.25s;
}
@keyframes animate2{
    0%{
        top: -100%;
    }
    50%,100%{
        top: 100%;
    }
}
a span:nth-child(3){
    bottom: 0;
    right: 0;
    width: 100%;
    height: 2px;
    background: linear-gradient(270deg,transparent,#03e9f4);
    animation: animate3 1s linear infinite;
    animation-delay: 0.50s;
}
@keyframes animate3{
    0%{
        right: -100%;
    }
    50%,100%{
        right: 100%;
    }
}


a span:nth-child(4){
    bottom: -100%;
    left: 0;
    width: 2px;
    height: 100%;
    background: linear-gradient(360deg,transparent,#03e9f4);
    animation: animate4 1s linear infinite;
    animation-delay: 0.75s;
}
@keyframes animate4{
    0%{
        bottom: -100%;
    }
    50%,100%{
        bottom: 100%;
    }
}

/*----------------框-----------------*/
@property --rotate {
  syntax: "<angle>";
  initial-value: 132deg;
  inherits: false;
}

:root {
  --card-height: 65vh;
  --card-width: calc(var(--card-height)/0.6);

   --bg: hsl(223deg, 10%, 90%);
   --trans-dur: 0.3s;
   font-size: calc(16px + 4 * (100vw - 320px) / 960);
}


body {
  min-height: 100vh;
  background: #212534;
  display: flex;
  align-items: center;
  flex-direction: column;
  padding-top: 0rem;
  padding-bottom: 0rem;
  box-sizing: border-box;
  
}


.card {
  background: #191c29;
 /* width: var(--card-width);*/
 /* height: var(--card-height);*/
  padding: 0px;
  position: relative;
  border-radius: 6px;
  justify-content: center;
  align-items: center;
  text-align: center;
  /*display: flex;*/
  font-size: 1.5em;
  color: rgb(88 199 250 / 100%);
  cursor: pointer;
  font-family: cursive;
}

.card:hover {
  color: #ffffff;
  transition: color 1s;
}
.card:hover:before, .card:hover:after {
  animation: none;
  opacity: 0;
}


.card::before {
  content: "";
  width: 104%;
  height: 102%;
  border-radius: 8px;
  background-image: linear-gradient(
    var(--rotate)
    , #5ddcff, #3c67e3 43%, #4e00c2);
    position: absolute;
    z-index: -1;
    top: -1%;
    left: -2%;
    animation: spin 2.5s linear infinite;
}

.card::after {
  position: absolute;
  content: "";
  top: calc(var(--card-height) / 6);
  left: 0;
  right: 0;
  z-index: -1;
  height: 100%;
  width: 100%;
  margin: 0 auto;
  transform: scale(0.8);
  filter: blur(calc(var(--card-height) / 6));
  background-image: linear-gradient(
    var(--rotate)
    , #5ddcff, #3c67e3 43%, #4e00c2);
    opacity: 1;
  transition: opacity .5s;
  animation: spin 2.5s linear infinite;
}

@keyframes spin {
  0% {
    --rotate: 0deg;
  }
  100% {
    --rotate: 360deg;
  }
}

/*----------------框-----------------*/

/*--------------两边----------------*/
.tvdd {
	overflow: hidden;
	position: relative;
          top: 5%;
	width: 16em;
	height: 16em;
}
.tvdd__ring {
	top: 0%;
	left: 38%;
	width: 30%;
	height: 30%;
	transform-origin: 50% 80%;
}
.tvdd__ring, .tvdd__ring-dot {
	position: absolute;
}
.tvdd__ring-dots {
	animation: pivot 1s linear infinite;
	width: 100%;
	height: 100%;
}
.tvdd__ring-dot {
	animation: pulse 1s ease-in-out infinite;
	background-color: hsl(193deg, 90%, 55%);
	border-radius: 50%;
	margin: -5% 0 0 -5%;
	width: 10%;
	height: 10%;
}
.tvdd__ring-dot:nth-child(1) {
	top: 38.3531429704%;
	left: 6.533337817%;
}
.tvdd__ring-dot:nth-child(2) {
	animation-delay: -0.0833333333s;
	top: 61.6468570296%;
	left: 6.533337817%;
}
.tvdd__ring-dot:nth-child(3) {
	animation-delay: -0.1666666667s;
	top: 81.8198051534%;
	left: 18.1801948466%;
}
.tvdd__ring-dot:nth-child(4) {
	animation-delay: -0.25s;
	top: 93.466662183%;
	left: 38.3531429704%;
}
.tvdd__ring-dot:nth-child(5) {
	animation-delay: -0.3333333333s;
	top: 93.466662183%;
	left: 61.6468570296%;
}
.tvdd__ring-dot:nth-child(6) {
	animation-delay: -0.4166666667s;
	top: 81.8198051534%;
	left: 81.8198051534%;
}
.tvdd__ring-dot:nth-child(7) {
	animation-delay: -0.5s;
	top: 61.6468570296%;
	left: 93.466662183%;
}
.tvdd__ring-dot:nth-child(8) {
	animation-delay: -0.5833333333s;
	top: 38.3531429704%;
	left: 93.466662183%;
}
.tvdd__ring-dot:nth-child(9) {
	animation-delay: -0.6666666667s;
	top: 18.1801948466%;
	left: 81.8198051534%;
}
.tvdd__ring-dot:nth-child(10) {
	animation-delay: -0.75s;
	top: 6.533337817%;
	left: 61.6468570296%;
}
.tvdd__ring-dot:nth-child(11) {
	animation-delay: -0.8333333333s;
	top: 6.533337817%;
	left: 38.3531429704%;
}
.tvdd__ring-dot:nth-child(12) {
	animation-delay: -0.9166666667s;
	top: 18.1801948466%;
	left: 18.1801948466%;
}
.tvdd__ring:nth-child(2) {
	transform: rotate(120deg);
}
.tvdd__ring:nth-child(2) .tvdd__ring-dot {
	background-color: hsl(223deg, 90%, 55%);
}
.tvdd__ring:nth-child(3) {
	transform: rotate(240deg);
}
.tvdd__ring:nth-child(3) .tvdd__ring-dot {
	background-color: hsl(253deg, 90%, 55%);
}

/* Dark theme */
@media (prefers-color-scheme: dark) {
	:root {
		--bg: hsl(223deg, 10%, 10%);
	}
}
/* Animations */
@keyframes pivot {
	from {
		transform: rotate(0);
	}
	to {
		transform: rotate(30deg);
	}
}
@keyframes pulse {
	from, to {
		transform: scale(0.1);
	}
	50% {
		transform: scale(1);
	}
}


/**/

/*--------------两边----------------*/
/*body {
  margin: 0;
  padding: 0;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #050801;
}*/





.container {
  display: grid; 
  grid-template-columns: 0.6fr 1.8fr; 
  grid-template-rows: 0.4fr auto; 
  gap: 0px 0px; 
  grid-template-areas: 
    "header header"
    "rcol article"; 
}
.article {
  display: grid; 
  grid-template-columns: 1fr 1fr 1fr; 
  grid-template-rows: 1.6fr; 
  gap: 0px 0px; 
  padding-top: 50px;
  padding-right: 150px;
  grid-template-areas: 
    "image image image"; 
  grid-area: article; 
}
.image { grid-area: image; }
.header { grid-area: header; }
.rcol {
  display: grid; 
  grid-template-columns: 1fr; 
  grid-template-rows: 0.9fr 0.9fr; 
  gap: 0px 0px; 
  grid-template-areas: 
    "buttons"
    "loading"; 
  grid-area: rcol; 
}
.buttons { 
  padding-top: 50px;
  grid-area: buttons;
 }
.loading { 
  grid-area: loading; 
  display: none;
}

.transbox
{
  /*position: fixed;
  top: 200px;
  bottom: 0px;
  right:350px;
  left:350px;*/
  margin:0px 0px;
  background-color:#ffffff;

  opacity:0.6;
  filter:alpha(opacity=60); /* IE8 及更早版本 */
}




.txt {
 	font-family: Courier New;
    white-space: pre-wrap;
    font-size: 60%;
    text-align: left
}

/*网站标题效果*/
h1 {
  color: #fff;
  font-family: sans-serif;
  font-size: 5em;
  text-align: center;
  animation: animate 0.5s linear infinite,hu__hu__ infinite 2s ease-in-out;
}

@keyframes animate {
  0%, 100% {
    text-shadow: -1.5px -1.5px 0 #0ff, 1.5px 1.5px 0 #f00;
  }
  25% {
    text-shadow: 1.5px 1.5px 0 #0ff, -1.5px -1.5px 0 #f00;
  }
  50% {
    text-shadow: 1.5px -1.5px 0 #0ff, 1.5px -1.5px 0 #f00;
  }
  75% {
    text-shadow: -1.5px 1.5px 0 #0ff, -1.5px 1.5px 0 #f00;
  }
} 

.hu__hu__ { animation: hu__hu__ infinite 2s ease-in-out }
@keyframes hu__hu__ {
    50% { transform: translateY(15px) }
}

 input {
     position: absolute;
     font-size: 100px;
     right: 0;
     top: 0;
     opacity: 0;
     filter: alpha(opacity=0);
     cursor: pointer;
 }

</style>
</head>

<body>
    


    <div class="container">
        <div class="header">

            <h1>ASCII art</h1>
        </div>
        <div class="rcol">
          <div class="buttons">
            <form enctype="multipart/form-data" 
                     action="/cgi-bin/new_post_img.py" method="post">
           
                <a>
                    <input type="file" name="filename"  value="Upload" />select
                </a>
           
          
                <a >
                    <input type="submit" onclick="toggle_visibility('load')" value="      " />submit
               </a> 
             </form> 
            </div>

<script>
  function toggle_visibility(id) {
       var e = document.getElementById(id);
       if(e.style.display == 'block')
          e.style.display = 'none';
       else
          e.style.display = 'block';
   }
</script>

    <div class="loading" id="load">
      <div class="tvdd" role="img" aria-label="Three intersecting rings of twelve pulsing dots that never collide">
	<div class="tvdd__ring">
		<div class="tvdd__ring-dots">
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
		</div>
	</div>
	<div class="tvdd__ring">
		<div class="tvdd__ring-dots">
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
		</div>
	</div>
	<div class="tvdd__ring">
		<div class="tvdd__ring-dots">
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
			<div class="tvdd__ring-dot"></div>
		</div>
	</div>
</div>
      </div>
           
             
       
        </div>



        <div class="article">

          <div class="image">
      
<div class="card">
 <p class="txt">
''' + text_img +'''
</p>
</div>
          </div>
        </div>
        
      </div>

</body>
</html>
'''#.format(text_img)
)
