/*!
  Lazy UI design, v1.0.0-21.
  Created by Edgar Gulay for the Lazy Messenger.
  License: Not licensed.

  Web front end UI js file.
  Modified to fit current usage.
  created on: 04 September 2021, 5:27 am.
*/


// media disable contextmenu

// respinsive adjustments

// page dimensions
var width = innerWidth
function dimensions() {
  $(".full_height").css({ "height": innerHeight + "px" })
  $(".full_width").css({ "width": innerWidth + "px" })
}
$('document').ready(function () { dimensions() })
document.body.onresize = function () { dimensions() }


// create message tab
function create_message(message) {
  // parent element
  var parent = getById("lazy_chat_room")
  // message row
  var message_row = newChild(parent, 'div', 'row_' + message.id, 'msg_row mt_5 p_10 fw')
  // user class name
  var user = null;
  if (message.sender_id != my_id) {
    user = 'rcver_msg float-left'
  } else {
    user = 'user_msg float-right'
  }

  // message container
  var msg_container = newChild(message_row, 'div', message.id, 'msg_container flex flex_col ' + user)


  if (message.text) {
    // message box
    var msg_box = newChild(msg_container, 'div', '', 'msg_box fw')
    // content
    var content = newChild(msg_box, 'p')
    writeIn(content, message.content)
  }

  if (message.video) {
    // message box
    var video_box = newChild(msg_container, 'div', '', 'video_box fw')
    // content
    var content = newChild(video_box, 'video', '', 'video_file ', 'src', '/static/' + message.content)
    content.controls = true
  }
  if (message.image) {
    // message box
    var image_box = newChild(msg_container, 'div', '', 'image_box fw')
    // content
    var content = newChild(image_box, 'img', '', 'image_file ', 'src', '/static/' + message.content)

  }

  // time info
  var time_span = newChild(msg_container, 'div', '', 'msg_info fw')
  var span = newChild(time_span, 'span', '', 'timespan')
  writeIn(span, message.time_sent)

  //delete button
  if (message.sender_id == my_id) {
    var delBut = newChild(time_span, 'a', message.id, 'delBut text-warning ion-ios-trash flt_right', 'href', '/main/del/' + message.id)
  }
}

//play video when clicked
$('.video_file ').click(function () { this.play() })

$('.delBut').on('click', function (e) {
  e.preventDefault()
  alert('hurray')
  console.log('working')
})





