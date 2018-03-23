$(function () {
    //　当用户点击一下图片，我们就在图片的url后面加一个?
    //　这样url改变就会触发浏览器再次请求生成图片，并且会
    // 重新设置cookie.
     $("#img_check_reg").click(function () {
        var src = $(this).attr("src");
        $(this).attr("src", src + "?")
    });
});