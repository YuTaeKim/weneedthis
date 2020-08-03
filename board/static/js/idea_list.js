
$('button.delete').click(function(){
    var pk=$(this).attr('name')
    $.ajax({
        type:"post",
        url:"{% url 'board:delete_comment' %}",
        data: {'pk':pk,'csrfmiddlewaretoken':'{{ csrf_token }}'},
        dataType:"json",
        success:function(response){
            comment = $('#delete'+pk).parents('div.single_comment');
            comment.remove();
        },
        error:function(request,status,error){
            alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
        }
    });
})



$('button.update').click(function(){
    var pk=$(this).attr('name')
    if($(this).hasClass('process')){
        $('#comment_article'+pk).show();
        $('#update_article'+pk).hide();
        $(this).removeClass('process');
    }
    else{
        $('#comment_article'+pk).hide();
        $('#update_article'+pk).show();
        $(this).addClass('process');
    }
})




$('button.update_process').click(function(){
    var pk=$(this).attr('name')
    var content=$('#update_comment'+pk).val()
    $.ajax({
        type:"post",
        url:"{% url 'board:update_comment' %}",
        data: {'content':content,'pk':pk,'csrfmiddlewaretoken':'{{ csrf_token }}'},
        dataType:"json",
        success:function(response){
            $('#comment_article'+pk).html(response.article);
            $('#comment_article'+pk).show();
            $('#update_article'+pk).hide();
            $('#update'+pk).removeClass('process');
        },
        error:function(request,status,error){
            alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
        }
    });
})



$('#add').click(function(){
    var pk=$(this).attr('name')
    var content=$('#comment').val()
    $.ajax({
        type:"post",
        url:"{% url 'board:add_comment' %}",
        data: {'content':content,'pk':pk,'csrfmiddlewaretoken':'{{ csrf_token }}'},
        dataType:"json",
        success:function(response){
            $('#plus_comment').append(response.html);
            $('#comment').val("");
        },
        error:function(request,status,error){
            alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
        }
    });
})



$('#idea').addClass("active");



$('div input[type=button]').click(function(){
    var pk=$(this).attr('name')
    $.ajax({
        type:"post",
        url:"{% url 'board:likes_process' %}",
        data: {'pk':pk,'csrfmiddlewaretoken':'{{ csrf_token }}'},
        dataType:"json",
        success:function(response){
            $('#count'+pk).html('&nbsp;'+response.message);
            if(response.flag==true){
                $('#button'+pk).css('color','red');
            }
            else{
                $('#button'+pk).css('color','black');     
            }
        },
        error:function(request,status,error){
            alert("code:"+request.status+"\n"+"message:"+request.responseText+"\n"+"error:"+error);
        }
    });
})
