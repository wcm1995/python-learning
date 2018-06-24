function byId(id){
	return typeof(id)==="string"?document.getElementById(id):id;  //检查id的类型
}
var index=0,
    timer=null,
    pics=byId("banner").getElementsByTagName("div"),
    dots=byId("dots").getElementsByTagName("span"),
    prev=byId("prev"),
    next=byId("next"),
    len=pics.length;

function slideImg(){
	var main=byId("main");
	main.onmouseover=function(){
		if(timer) clearInterval(timer);
	}
	main.onmouseout=function(){
		timer=setInterval(function(){
			index++;
			if(index>=len){
            	index=0;
			}
			//切换图片
			changeImg();
		},2000);
	}
	//自动在main上触发鼠标离开的事件
	main.onmouseout();

	//遍历所有点击，且绑定点击事件，点击圆点切换图片
	for(var d=0;d<len;d++){
		//给所有span添加一个id属性，值为d，作为span的索引
		dots[d].id=d;
		dots[d].onclick=function(){
			index=this.id;
			changeImg();
		}
	}

	//下一张
	next.onclick=function(){
		index++;
		if(index>=len) index=0;
		changeImg();
	}

	//上一张
	prev.onclick=function(){
		index--;
		if(index<0) index=len-1;
		changeImg();
	}

}

//切换图片
function changeImg(){
	//遍历banner下所有的div，将div隐藏
	//遍历dots下所有的span，清除类
	for(var i=0;i<len;i++){
		pics[i].style.display="none";
		dots[i].className="";
	}
	//根据index索引，找到当前div和span，将其显示出来并设为当前
	pics[index].style.display='block';
	dots[index].className="active";
}
slideImg();