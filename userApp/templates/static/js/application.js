$(document).ready(function() {

    $('.dropdown-toggle').dropdown();

    $('#action_button').click(
        function(){
            hello_js();
        }
    );

    function hello_js(){
        $.ajax({
            type:'GET',
            dataType: 'json',
            url: '/get_hello_world',
            success: (data) => {
                    $('#hello_js').html(data['text'])
                }
            });
    }
});
