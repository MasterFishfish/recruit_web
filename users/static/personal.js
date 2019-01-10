$('#submitbutton').on('click', function(e){
   // 获得表单的输入
//   var _unameValue = $("#Job").val();
//   var _emailValue = $("#email").val();
//   var _passValue = $("#TelNumber").val();
   alert("python后端工程师适合你")
   // var thedata = {"username": _unameValue , "email": _emailValue , "password":_passValue};
   // 逻辑判断
   //向服务器发送数据注册用户
//   $.ajax({
//           url:"/register/",
//           type:"post",
//           dataType: 'json',
//           data: thedata,
//           success:function(response){
//               if(response["code"] == 400){
//                alert(response["message"])
//               }
//               if(response["code"] == 200){
//                //alert(response["message"] + "...点击确定继续")
//                alert("恭喜您注册成功，请使用新账号登录");
//               }
////               if(response[]) {
////                  alert("用户名存在，请使用其他账号注册");
////                } else {
////                   alert("恭喜您注册成功，请使用新账号登录");
////                   location.href = "login.html";
////                }
//                },
//           error:function() {
//                        alert("系统繁忙，请稍后再试...");
//                    }
//                });
});

$('.container').find('input, textarea').on('keyup blur focus', function (e) {
  
  var $this = $(this),
      label = $this.prev('label');

	  if (e.type === 'keyup') {
			if ($this.val() === '') {
          label.removeClass('active highlight');
        } else {
          label.addClass('active highlight');
        }
    } else if (e.type === 'blur') {
    	if( $this.val() === '' ) {
    		label.removeClass('active highlight'); 
			} else {
		    label.removeClass('highlight');   
			}   
    } else if (e.type === 'focus') {
      
      if( $this.val() === '' ) {
    		label.removeClass('highlight'); 
			} 
      else if( $this.val() !== '' ) {
		    label.addClass('highlight');
			}
    }

});

$('.tab a').on('click', function (e) {
  
  e.preventDefault();
  
  $(this).parent().addClass('active');
  $(this).parent().siblings().removeClass('active');
  
  target = $(this).attr('href');

  $('.tab-content > div').not(target).hide();
  
  $(target).fadeIn(600);
  
});

