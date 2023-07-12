function get_page_data(){ 
    //this function gets the Auto OWL status/data and shows that on the website with the update_page(data) function
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://localhost:7676/api/get_status/", true);

    xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
        var response = xhr.responseText;
        console.log(response)
        update_page(response.split("|||")[0].split("|"),response.split("|||")[1].split("|"))
    }
    };
    xhr.send();
}

function update_page(data,error_msgs){
    stream_status = ""
    url = data[0]
    is_streaming = false
    if (data[0] == "0"){
      stream_status = "⚫ Auto OWL is currently not streaming.";
  }else if (data[0] == "launching"){
    stream_status = "🟢 Auto OWL is loading...";
}else{
        stream_status = "🔴 Auto OWL is currently watching stream.";
        is_streaming = true;
    }

    if (data[5] == "0"){
        document.getElementById("main-container").innerHTML = `<div style="background-color: white; width:500px; padding-bottom: 1px; border-radius: 5px; transform: translate(-50%,0);">
        <p style="text-align: center;padding-top: 15px;">No data available. Either Auto OWL is about to launch, or not running at all. Please wait a few seconds and try again.</p>
      </div>`;
      return;
        
    }

    html_if_streaming = `
    <div style="background-color: white; width:500px; padding-bottom: 1px; border-radius: 5px; transform: translate(-50%,0);">
      <p style="text-align: center;padding-top: 15px;">` + stream_status + `</p>
    </div>
    <div style="background-color: white; width:500px; padding-bottom: 1px; border-radius: 5px; transform: translate(-50%,0);">
      <h2 style="text-align: center;">Current session stats:
      </h2>
      <p style="text-align: center;">💵 Tokens earnt this session (estimation): ` + data[1] + `<br><br>⏰ Time watched this session: ` + data[2] + `<br><br>Stream URL: <a href="` + url + `">` + url + `</a></p>
    </div><div style="background-color: white; width:500px; padding-bottom: 1px; border-radius: 5px; transform: translate(-50%,0);">
      <h2 style="text-align: center;">All time stats:
      </h2>
      <p style="text-align: center;">💵 Tokens earnt all time (estimation): ` + data[3] + `<br><br>⏰ Time watched all time: ` + data[4] + `</p>
    </div>`

    html_if_not_streaming = `
    <div style="background-color: white; width:500px; padding-bottom: 1px; border-radius: 5px; transform: translate(-50%,0);">
      <p style="text-align: center;padding-top: 15px;">` + stream_status + `</p>
    </div>
    <div style="background-color: white; width:500px; padding-bottom: 1px; border-radius: 5px; transform: translate(-50%,0);">
      <h2 style="text-align: center;">All time stats:
      </h2>
      <p style="text-align: center;">💵 Tokens earnt all time (estimation): ` + data[3] + `<br><br>⏰ Time watched all time: ` + data[4] + `</p>
    </div>`

    html = ""
    if(is_streaming){
        html = html_if_streaming;
    }else{
        html = html_if_not_streaming
    }
  
  document.getElementById("main-container").innerHTML = html;
  if(error_msgs != ""){

  error_msgs.forEach(element => {
    show_error(element);
  });
}}

function show_error(element){
    document.getElementById("main-container").innerHTML += `<div style="background-color: #e64051; width:500px; padding-bottom: 1px; border-radius: 5px; transform: translate(-50%,0);">
    <p id="error-to-fix" style="text-align: center;padding-top: 15px;"></p>
  </div>`;
  document.getElementById("error-to-fix").textContent = element;
  document.getElementById("error-to-fix").innerHTML = `<b>Error: </b>` + document.getElementById("error-to-fix").innerHTML
  document.getElementById("error-to-fix").id = "error-fixed"
}

function longPoll() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/api/connect', true);
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                var data = JSON.parse(xhr.responseText);
                data_text = data.text.split("|:|: ")[1];
                if(data.text.startsWith("e|:|: ")){
                    show_error(data_text)
                }else if(data.text.startsWith("s|:|: ")){
                    update_page(data_text.split("|||")[0].split("|"),data_text.split("|||")[1].split("|"))
                }
                longPoll();  // Make the next request
            } else {
                if (xhr.status === 0) {
                    longPoll();
                }
            }
        }
    };
    xhr.timeout = 60000;  // Timeout after 60 seconds
    xhr.ontimeout = function() {
        longPoll(); 
    };
    xhr.send();
}

longPoll();
get_page_data(); //initially get the data and errors 
