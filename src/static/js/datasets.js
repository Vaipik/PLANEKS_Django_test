$(function ($) {
    $("button").click(function (event) {
        const button_id = this.id.match(/\d+/)[0];
        const button_type = this.id.match(/[a-z_]+/)[0]
        if (button_type === "modal_button") {
            $("#delete_file" + button_id).submit(function (event) {
                event.preventDefault()
                $.ajax({
                    type: this.method,
                    url: this.action,
                    data: $(this).serialize(),
                    dataType: 'json',
                    success: function (response) {
                        console.log(response)
                        if (response.status === 204) {
                            window.location.reload()
                        }
                    },
                    error: function (response) {
                        console.log('error' - response)
                    }
                })
            })
        } else {
            $("#generate_csv" + button_id).submit(function (event) {
                event.preventDefault()
                $(`.dataset${button_id}`).removeClass('bg-success').addClass('bg-danger').text("GENERATING")
                $.ajax({
                    type: this.method,
                    url: this.action,
                    data: $(this).serialize(),
                    dataType: 'json',
                    success: function (response) {
                        console.log(response)
                        if (response.status === 201) {
                            window.location.reload()
                            $(`.dataset${button_id}`).removeClass('bg-danger').addClass('bg-success').text("Generated")

                        }
                    },
                    error: function (response) {
                        console.log('error' - response)
                    }
                })
            })
        }
    })
})