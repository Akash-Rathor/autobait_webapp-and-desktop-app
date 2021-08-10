document.addEventListener("DOMContentLoaded", function(){
// make it as accordion for smaller screens
if (window.innerWidth > 992) {

	document.querySelectorAll('.navbar .nav-item').forEach(function(everyitem){

		everyitem.addEventListener('mouseover', function(e){

			let el_link = this.querySelector('a[data-bs-toggle]');

			if(el_link != null){
				let nextEl = el_link.nextElementSibling;
				el_link.classList.add('show');
				nextEl.classList.add('show');
			}

		});
		everyitem.addEventListener('mouseleave', function(e){
			let el_link = this.querySelector('a[data-bs-toggle]');

			if(el_link != null){
				let nextEl = el_link.nextElementSibling;
				el_link.classList.remove('show');
				nextEl.classList.remove('show');
			}

		})
	});

}
// end if innerWidth
}); 
//---------------
$('#myTab a').on('click', function (event) {
  event.preventDefault()
  $('#myTab').find('.active').removeClass('active');
  $(this).tab('show')
})
//------------
$('.dtlOfdots .clickDtlOftable').click(function(e){
	e.stopPropagation();
	$('.dtlOfdots .sideDotsDtl').hide();
	$(this).next('.sideDotsDtl').toggle();
})
$('body').click(function(e){
	e.stopPropagation();
	$('.dtlOfdots .sideDotsDtl').hide();
})
//-----linkedin Url - lead range-------
class Slider {
  constructor (rangeElement, valueElement, options) {
    this.rangeElement = rangeElement
    this.valueElement = valueElement
    this.options = options

    // Attach a listener to "change" event
    this.rangeElement.addEventListener('input', this.updateSlider.bind(this))
  }

  // Initialize the slider
  init() {
    this.rangeElement.setAttribute('min', options.min)
    this.rangeElement.setAttribute('max', options.max)
    this.rangeElement.value = options.cur

    this.updateSlider()
  }

  // Format the money
  asMoney(value) {
    return parseFloat(value)
      .toLocaleString('en-US', { maximumFractionDigits: 2 })
  }

  generateBackground(rangeElement) {   
    if (this.rangeElement.value === this.options.min) {
      return
    }

    let percentage =  (this.rangeElement.value - this.options.min) / (this.options.max - this.options.min) * 100
    return 'background: linear-gradient(to right, #ffbe0f, #ffbe0f ' + percentage + '%,  ' + percentage + '%, #dee1e2 100%)'
    // return 'background: linear-gradient(to right, #50299c, #7a00ff ' + percentage + '%, #d3edff ' + percentage + '%, #dee1e2 100%)'
  }

  updateSlider (newValue) {
    this.valueElement.innerHTML = this.asMoney(this.rangeElement.value)
    this.rangeElement.style = this.generateBackground(this.rangeElement.value)
  }
}

let rangeElement = document.querySelector('.range [type="range"]')
let valueElement = document.querySelector('.range .range__value span') 

let options = {
  min: 10,
  max: 1000,
  cur: 250
}

if (rangeElement) {
  let slider = new Slider(rangeElement, valueElement, options)

  slider.init()
}
//---------------------------
$(document).on('input', '.inerRange', function() {
    $(this).next('.slider_value').html( $(this).val() );
});
//----------------
$('.eyeBox').click(function(){
  $(this).toggleClass('showEye');
})
//------------------
function viewfunction() {
  var temp = document.getElementById("tokenid");
  if (temp.type === "text") {
    temp.type = "password";
  }
  else {
    temp.type = "text";
  }
}
function viewfunction1() {
  var temp = document.getElementById("linkedinpass");
  if (temp.type === "text") {
    temp.type = "password";
  }
  else {
    temp.type = "text";
  }
}
function urlvalidator(){
  var inputurl = document.getElementById("searchedurl").value;
  if (inputurl.includes("https://linkedin.com")||inputurl.includes("https://www.linkedin.com/"))
  {
    if (inputurl.includes('FACETED_SEARCH&')||inputurl.includes('SWITCH_SEARCH_VERTICAL')||inputurl.includes('FACETED_SEARCH')||inputurl.includes('CLUSTER_EXPANSION')){
      document.getElementById('msg').innerHTML = 'Valid URL';
      document.getElementById('msg').style.display = 'block';
      document.getElementById('msg').style.color = 'Green';
      $('button').prop('disabled', false);
    }
  }
  else {
    document.getElementById('msg').innerHTML = 'Invalid URL';
    document.getElementById('msg').style.display = 'block';
    document.getElementById('msg').style.color = 'red';
    $('button').prop('disabled', true);
  }
}
//--------------------
// $(document).ready(function(){
//   $('#sortable-div .sortable-list').sortable({
//    connectWith: '#sortable-div .sortable-list',
//     placeholder: 'placeholder',
//  });
// });


$('.listOfCamp_Newtouch a').click(function(){
  var getid = $(this).attr('id');
  var proEng = $('#allBoxHere').find('.profileEngeg01').length;
  var linkCont = $('#allBoxHere').find('.linkedConnect01').length;
  var linkMesg = $('#allBoxHere').find('.linkedMessage01').length;
    var linkCont1 = $('.linkedConn1').length;

  var sort_item=$(".prof_Engag").length+1;
  if(getid !== '') {
    if (getid == "profileEngeg") {
      if(proEng == 0){
        $('#allBoxHere').append('<div class="prof_Engag linkedConn sortable-item mt-5"><div class="titleOfNewTouch"><span class="moveBox"><i class="fa fa-arrows-alt" aria-hidden="true"></i><em>'+sort_item+'</em></span><h2><span>Engage with profile</span><div class="dayStep"><div class="reqConnect"><input type="text" class="form-control"><select name="days"><option>days</option></select></div><span>from previous step.</span></div></h2><span class="cancelBox"><i class="fa fa-times" aria-hidden="true"></i></span></div><div class="formEngag"><div class="checkBtnMain"><div class="toggle-button-cover"><div class="button-cover"><div class="onOffBtn r" id="button-1"><input type="checkbox" class="checkbox" name="Visit_LinkedIn_Profile"><div class="knobs"></div><div class="layer"></div></div></div></div><span>Visit LinkedIn Profile</span></div><div class="checkBtnMain"><div class="toggle-button-cover"><div class="button-cover"><div class="onOffBtn r" id="button-1"><input type="checkbox" name="Auto_Follow_on_LinkedIn" class="checkbox"><div class="knobs"></div><div class="layer"></div></div></div></div><span>Auto Follow on LinkedIn</span></div><div class="checkBtnMain"><div class="toggle-button-cover"><div class="button-cover"><div class="onOffBtn r" id="button-1"><input type="checkbox" name="Auto_Follow_on_LinkedIn" class="checkbox"><div class="knobs"></div><div class="layer"></div></div></div></div><span>Auto Follow on LinkedIn</span></div><div class="checkBtnMain"><div class="toggle-button-cover"><div class="button-cover"><div class="onOffBtn r" id="button-1"><input type="checkbox" name="Auto_Follow_on_LinkedIn" class="checkbox"><div class="knobs"></div><div class="layer"></div></div></div></div><span>Auto Follow on LinkedIn</span><select><option>1</option><option>2</option><option>3</option></select></div><div class="engProfAddtag"><div class="checkBtnMain"><div class="toggle-button-cover"><div class="button-cover"><div class="onOffBtn r" id="button-1"><input type="checkbox" name="Add_tags_in_this_step" class="checkbox"><div class="knobs"></div><div class="layer"></div></div></div></div><span>Add tags in this step</span></div><div class="alfredCrmBox"><div class="checkBtnMain">Add Tags to Alfred CRM</div><div class="innerAlfCrm"><input type="text" class="form-control" name="Select_Alfred_Tags" placeholder="Select Alfred Tags" /><input type="text" class="form-control" name="Create_new_tag" placeholder="Create new tag" /></div></div></div></div></div>')
      } 
    } else if (getid == "linkConnect") {
      if(linkCont == 0){              
        $('#allBoxHere').append('<div class="prof_Engag linkedConn1 sortable-item mt-5"><div class="titleOfNewTouch"> <span class="moveBox"> <i class="fa fa-arrows-alt" aria-hidden="true"></i> <em>'+sort_item+'</em> </span><h2> <span>Send a connection request</span><div class="dayStep"><div class="reqConnect"> <input type="text" name="dayNum" class="form-control"> <select name="days"><option>days</option> </select></div> <span>from previous step.</span></div></h2> <span class="cancelBox"><i class="fa fa-times" aria-hidden="true"></i></span></div><div class="formEngag"><div class="form-group"><div class="connectReqMsg"><div class="conReqText">Connection Request Message</div><div class="conReqMsgBtn"> <button type="button" class="button" data-bs-toggle="modal" data-bs-target="#linkedInConnect02Modal">Templates</button><div class="btn-group"><button type="button" class="btn button dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false"> Personalize </button><div class="dropdown-menu dropdown-menu-end personalDropBox"><h3>SNIPPETS</h3><div class="inerDrop" id="mess_c_1"> <a class="dropdown-item" href="javascript:void(0)">First Name</a> <a class="dropdown-item" href="javascript:void(0)">Last Name</a> <a class="dropdown-item" href="javascript:void(0)">Company</a> <a class="dropdown-item" href="javascript:void(0)">Position</a> <a class="dropdown-item" href="javascript:void(0)">Industry</a></div></div></div></div></div><div class="msgOfContReq"><textarea rows="5" id="con_textarea" name="Connection-Request-Message" class="form-control conarea"></textarea><small>Alfred will cut the message if it exceeds 300 characters adding the snippets</small></div></div><div class="engProfAddtag border-0 mt-3"><div class="checkBtnMain"><div class="toggle-button-cover"><div class="button-cover"><div class="onOffBtn r" id="button-1"> <input type="checkbox" name="Auto-follow-up-with-message-once-connected" class="checkbox"><div class="knobs"></div><div class="layer"></div></div></div></div> <span>Auto follow-up with message once connected</span></div><div class="autoFollowDtlBox"><div class="connectReqMsg"><div class="conReqText">Follow Up Message After Connect</div><div class="conReqMsgBtn"> <button type="button" class="button" data-bs-toggle="modal" data-bs-target="#linkedInConnect02Modal">Templates</button><div class="btn-group"> <button type="button" class="btn button dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false"> Personalize </button><div class="dropdown-menu dropdown-menu-end personalDropBox"><h3>SNIPPETS</h3><div class="inerDrop" id="mess_c_2"> <a class="dropdown-item" href="javascript:void(0)">First Name</a> <a class="dropdown-item" href="javascript:void(0)">Last Name</a> <a class="dropdown-item" href="javascript:void(0)">Company</a> <a class="dropdown-item" href="javascript:void(0)">Position</a> <a class="dropdown-item" href="javascript:void(0)">Industry</a></div></div></div></div></div><div class="msgOfContReq"><textarea rows="5" name="Follow-Up-Message-After-Connect" class="form-control" id="mess_2"></textarea></div></div></div><div class="engProfAddtag mt-4"><div class="checkBtnMain"><div class="toggle-button-cover"><div class="button-cover"><div class="onOffBtn r" id="button-1"> <input type="checkbox" class="checkbox"><div class="knobs"></div><div class="layer"></div></div></div></div> <span>Auto follow-up with message once connected</span></div><div class="alfredCrmBox"><div class="checkBtnMain">Add Tags to Alfred CRM</div><div class="innerAlfCrm"> <input type="text" class="form-control" name="Select-Alfred-Tags" placeholder="Select Alfred Tags" /> <input type="text" class="form-control" name="Create-new-tag" placeholder="Create new tag" /></div></div></div></div></div>');
      } 
      $('#'+getid).addClass('disabled');
    } else if (getid == "linkMsg") {
      if(linkMesg == 0){
        $('#allBoxHere').append('<div class="prof_Engag linkedConn sortable-item mt-5"><div class="titleOfNewTouch"> <span class="moveBox"> <i class="fa fa-arrows-alt" aria-hidden="true"></i> <em>'+sort_item+'</em> </span><h2> <span>Send a message</span><div class="dayStep"><div class="reqConnect"> <input type="text" name="dayNum" class="form-control"> <select name="days"><option>days</option> </select></div> <span>from previous step.</span></div></h2> <span class="cancelBox"><i class="fa fa-times" aria-hidden="true"></i></span></div><div class="formEngag"><div class="form-group"><div class="connectReqMsg"><div class="conReqText">Send Linkedin message</div><div class="conReqMsgBtn"><div class="button attachFile"> <input type="file" name="fileName" /> <i class="fa fa-paperclip" aria-hidden="true"></i></div> <button type="button" class="button" data-bs-toggle="modal" data-bs-target="#linkedInMsg02Modal">Templates</button><div class="btn-group"> <button type="button" class="btn button dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false"> Personalize </button><div class="dropdown-menu dropdown-menu-end personalDropBox"><h3>SNIPPETS</h3><div class="inerDrop"> <a class="dropdown-item" href="javascript:void(0)">First Name</a> <a class="dropdown-item" href="javascript:void(0)">Last Name</a> <a class="dropdown-item" href="javascript:void(0)">Company</a> <a class="dropdown-item" href="javascript:void(0)">Position</a> <a class="dropdown-item" href="javascript:void(0)">Industry</a></div></div></div></div></div><div class="msgOfContReq"><textarea rows="5"  name="Send-Linkedin-message" class="form-control conarea"></textarea><small>Messages will only be sent to 1st degree connections. If the lead is not connected the message will be skipped.</small></div></div><div class="engProfAddtag mt-4"><div class="checkBtnMain"><div class="toggle-button-cover"><div class="button-cover"><div class="onOffBtn r" id="button-1"> <input type="checkbox" name="Add-Tags-to-Alfred-CRM" class="checkbox"><div class="knobs"></div><div class="layer"></div></div></div></div> <span>Add tags in this step</span></div><div class="alfredCrmBox"><div class="checkBtnMain">Add Tags to Alfred CRM</div><div class="innerAlfCrm"> <input type="text" class="form-control" name="Select-Alfred-Tags" placeholder="Select Alfred Tags" /> <input type="text" class="form-control" name="Create-new-tag" placeholder="Create new tag" /></div></div></div></div></div>');
      };
    }
    
    $('.engProfAddtag .checkbox').click(function(){
      $(this).parents('.engProfAddtag').toggleClass('activBtn').slow();
    });

    $('.titleOfNewTouch .cancelBox').click(function(){
      // $(this).parents('.prof_Engag').hide();
      $(this).parents('.prof_Engag').closest(".prof_Engag").remove();
		  if($(this).parents('.prof_Engag').closest(".linkedConn1").length>0){
			 $("#linkConnect").removeClass("disabled");  
		  } 

      $('#allBoxHere .prof_Engag:first-child .titleOfNewTouch .dayStep').hide();
      $('.prof_Engag').each(function(i){
        var li_no=i+1;
        //$(this).html(i + 1);
        $(this).children().children().children('em').html(li_no);
      });
    });

    $(".btn-group").click(function(e){ 
      e.stopPropagation();

      $(this).find(".dropdown-menu").addClass('show');
    });

    $('body').click(function() {
      $(".prof_Engag .dropdown-menu").removeClass('show');
   });
   

    $(".prof_Engag .dropdown-item").click(function(e){
     // $(".prof_Engag  .dropdown-menu").toggleClass('show');
     $(this).closest('.prof_Engag').find('.dropdown-menu').removeClass('show');
      e.stopPropagation();
      e.stopImmediatePropagation();

      var con_textarea_data='';
     //var con_textarea= $(".linkedConn1 .msgOfContReq #con_textarea").text();
     var closest_id =$(this).closest('.inerDrop').attr('id');

     if(closest_id=='mess_c_2'){ 
      var con_textarea =$("#mess_2").val();
     } 
     else {
       var con_textarea =$(this).closest('.prof_Engag').find('textarea.form-control').val();
     }  
     console.log("sdsdsds",con_textarea);
     if($(this).text()=='First Name'){
       con_textarea_data=con_textarea+"{{fname}}";
     }
     if($(this).text()=='Last Name'){
      con_textarea_data=con_textarea+"{{lname}}";
     }
     if($(this).text()=='Company'){
      con_textarea_data=con_textarea+"{{company}}";
     }
     if($(this).text()=='Position'){
      con_textarea_data=con_textarea+"{{position}}";
     }
     if($(this).text()=='Industry'){
      con_textarea_data=con_textarea+"{{industry}}";
     }


     //console.log("my test",con_textarea_data)
     //console.log("ssssss",$(this).closest('.formEngag').children().children('.msgOfContReq').children('.form-control').html())
     if(closest_id=='mess_c_2'){
       $("#mess_2").val(con_textarea_data);
     } else {
        $(this).closest('.prof_Engag').find('textarea.conarea').val(con_textarea_data);
     }
     //$(this).closest('.prof_Engag').find('textarea.form-control').html(con_textarea_data);
    //  $(".linkedConn1 .msgOfContReq #con_textarea").html(con_textarea_data);
    // $(this).off('click');   //or $(this).unbind()

    });

    

    $('#sortable-div .sortable-list').sortable({
      connectWith: '#sortable-div .sortable-list',
      placeholder: 'placeholder',
	  helper: 'clone',
		sort: function(e, ui) {
			//$(ui.placeholder).html(Number($("#sortable-div > .prof_Engag:visible").index(ui.placeholder)) + 1);
		},
		update: function(event, ui) {
			var $lis = $(this).children('.prof_Engag');
			$lis.each(function() {
				var $li = $(this);
				var newVal = $(this).index() + 1;
				console.log("newVal ",newVal);
				$(this).children().children().children('em').html(newVal);
			});
		}
    });
  }

});



