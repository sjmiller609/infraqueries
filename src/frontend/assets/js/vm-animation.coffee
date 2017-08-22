#
#
# makeNewPosition = ->
#
#     # Get viewport dimensions (remove the dimension of the div)
#     h = $(window).height() - 50;
#     w = $(window).width() - 50;
#
#     nh = Math.floor(Math.random() * h);
#     nw = Math.floor(Math.random() * w);
#
#     return [nh,nw];
#
# }
#
# animateCloud = ->
#     newq = makeNewPosition()
#     oldq = $('.a').offset()
#     speed = calcSpeed([oldq.top, oldq.left], newq)
#
#     $('.a').animate({ top: newq[0], left: newq[1] }, speed, function(){
#       animateDiv()
#     });
#
#
# calcSpeed(prev, next) = ->
#
#     x = Math.abs(prev[1] - next[1]);
#     y = Math.abs(prev[0] - next[0]);
#
#     greatest = x > y ? x : y;
#
#     speedModifier = 0.1;
#
#     speed = Math.ceil(greatest/speedModifier);
#
#     return speed;
