$(function () {
    //分页点击
    $('.pages a').click(function () {
        $('.pages a').eq($(this).index()).addClass('active').siblings().removeClass('active');
    });
     
//    var colorList = ['#F65087','#329768','#FB8052','#3693CA','#68C999','#109691'];
	var colorList = ['#100719','#045FB4','#610B4B','#BDBDBD','#FBFBEF','#173B0B'];
    $('.sort li').each(function (i) {
        $(this).css({background:colorList[i%5]});
    });
});
