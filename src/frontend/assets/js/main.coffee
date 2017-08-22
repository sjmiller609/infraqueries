vms = []

CallMethod = ->
   $.getJSON('http://flask-env.bxaftkmkem.us-west-2.elasticbeanstalk.com//state',
   {
      access_key: "0000",
      secret_key: "0000"
   },
   (data) ->
     vms = data
   )

# loads the vms to the html
loadVms = ->

  CallMethod()

  # wait 100 ms for aws call back
  setTimeout () ->
    $(".cloud-container").empty()
    cloudShape = $ "<div>"
    cloudShape.addClass "cloud-shape"
    $(".cloud-container").append cloudShape

    for vm in vms

      vmString = JSON.stringify(vm)
      az = vm.az
      name = vm.name

      newVM = $ "<div>"
      newVM.addClass "vm-container"
      newVMContent = $ "<div onclick=vmClick(\'" + vmString + "\')>"
      newVMContent.addClass "vm"
      newVMContent.addClass "vm-text"

      newVMContent.text(az + ", " + name)

      newVM.append newVMContent
      #newCl.append newVM

      $(".cloud-container").append newVM
      console.log "cloud updated"
  , 1000

root = exports ? this
root.vmClick = (vm) ->
  $(".modal").show();
  $(".vm-name").text(vm)

$(document).ready ->
  loadVms()
  # update every 10 seconds
  setInterval () ->
    loadVms()
  , 10000
