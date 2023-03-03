$(function ($) {
    let dataset_id = "";
    $("button").click(function (event) {
        dataset_id = this.id.match(/\d+/)[0];
        $("#generate_csv" + dataset_id).submit(function (event) {
            event.preventDefault()
            $(`.dataset${dataset_id}`).removeClass('bg-success').addClass('bg-danger').text("GENERATING")
            $.ajax({
                type: this.method,
                url: this.action,
                data: $(this).serialize(),
                dataType: 'json',
                success: function (response) {
                    console.log(response)
                    if (response.status === 201) {
                        window.location.reload()
                        $(`.dataset${dataset_id}`).removeClass('bg-danger').addClass('bg-success').text("Generated")

                    }
                },
                error: function (response) {
                    console.log('error' - response)
                }
            })
        })
    })

})