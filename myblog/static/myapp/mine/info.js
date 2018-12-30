// 隐藏源码中的评论，点赞，收藏标签，不需要
$(".post-adds").find('span').css('display','none');
$(function(){

  beautiful_soup()
  
  var $span = $("#talk").find("span")
  $span.on('click',function(){
    // 获取文章id
    var POST_ID = $("#post_id").text()

    // 点赞
    if($(this).index()==0){
      var $font = $(this).find("font")
      
      var point_old_num = $.trim($font.text());
      
      if(isNaN(point_old_num)){
        point_old_num = 0;
      }
      $font.text(parseInt(point_old_num)+1);
      // 后台更新数据库 
      ajax_handle('point', POST_ID)

    }

    // 收藏
    if ($(this).index()==1) {
      var $font = $(this).find("font")
      
      var mark_old_num = $.trim($font.text());
      
      if(isNaN(mark_old_num)){
        mark_old_num = 0;
      }
      $font.text(parseInt(mark_old_num)+1);
       ajax_handle('bookmark', POST_ID)
    }

    // 评论
    if($(this).index()==2){          
      // 获取用户，判断是否是登录状态
      var USER = $("#userhidden").text()
      var is_login = $.trim(USER)
      // 如果是不登录的状态下，不能评论，给出提示
      if(is_login.length==0){
         // 显示提示
        $("#tip").text("请先到<个人认证>登录").css("color","red").fadeIn(0).fadeOut(1000)
        return false;
      }
      $("#comment-box").css("display","block")
      $("#add-up").on("click", function(){

        var text = $("#comment-text").val()
        if (text.length<=0){
          // 显示提示
          $("#tip").css("color",'red').text("我不知道你要夸我什么？")
          .fadeIn(0).fadeOut(1000)
          return false;
        }
        var num = $(this).find("font").val()
        ajax_handle('comment', POST_ID, text)
      })
      $("#clean").on("click", function(){
        $("#comment-text").val('')
      })


    }

  })

})

function ajax_handle(option, post_id, text=null){
    
       
        $.ajax({
            type:'post',
            url: '/upgrate_post/',
            dataType: 'text',
            data:{
                'option': option,
                'text':text,
                'post_id':post_id
            },
            success: function (dt) {

              if(option == "comment"){
                  // 刷新页面
                  window.location.reload()
                  return false

                }else if(option == "point"){
                  // 显示提示
                  msg = "点赞成功"
                  
                 
                }else if(option == "bookmark"){
                   // 显示提示
                 msg = "收藏成功"
                }
                $("#tip").css("color",'blue').text(msg)
                  .fadeIn(0).fadeOut(2000)
                
            },
            error:function(er){
                if(option == "comment"){
                  // 显示提示
                  
                  $("#tip").css("color",'red').text("评论失败")
                  .fadeIn(0).fadeOut(2000)
                  $("#comment-text").val('')
                  return false;

                }else if(option == "point"){
                  // 显示提示
                  msg = "点赞失败"
                  
                 
                }else if(option == "bookmark"){
                   // 显示提示
                 msg = "收藏失败"
                }
                $("#tip").css("color",'red').text(msg)
                  .fadeIn(0).fadeOut(2000)

                return false;
                
            }

          })
    }

function beautiful_soup() {

  var $crayon = $(".crayon-syntax")

for(var i=0;i<$crayon.length;i++){
    var $textarea = $($crayon[i]).find("textarea")
    var pull = $textarea.text()
    $($crayon[i]).before("<pre>"+pull+"</pre>")
    $($crayon[i]).remove()
  }
 
}

