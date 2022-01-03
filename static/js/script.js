// This function is for materialize. This the mobile nav, modal, form select and datepicker to function correctly

$(document).ready(function () {
    $(".sidenav").sidenav({
        edge: "right",
        draggable: true
    });
    $('.modal').modal();
    $(".collapsible").collapsible();
    $(".tooltipped").tooltip();
    $("select").formSelect();
    $(".datepicker").datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 100,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });

    validateMaterializeSelect();

    function validateMaterializeSelect() {
        let classValid = {
            "border-bottom": "1px solid #4caf50",
            "box-shadow": "0 1px 0 0 #4caf50"
        };
        let classInvalid = {
            "border-bottom": "1px solid #f44336",
            "box-shadow": "0 1px 0 0 #f44336"
        };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({
                "display": "block",
                "height": "0",
                "padding": "0",
                "width": "0",
                "position": "absolute"
            });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () {})) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});


// This function is to display different options when a certain category is selected. CREDIT: https://jsfiddle.net/uftr0qa4/2/

var categoryEdit = document.querySelector("#category_name");
var attendedTargetEdit = document.getElementById("attendedSelectedEdit");
var upcomingTargetEdit = document.getElementById("upcomingSelectedEdit");

category.addEventListener("change", function () {
    if (categoryEdit.value == "Attended") {
        attendedTargetEdit.style = "display: block;";
        upcomingTargetEdit.style = "display: none;";
    } else if (categoryEdit.value == "Upcoming") {
        upcomingTargetEdit.style = "display: block;";
        attendedTargetEdit.style = "display: none;";
    }
})

var categoryAdd = document.querySelector("#category_name");
var attendedTargetAdd = document.getElementById("attendedSelectedAdd");
var upcomingTargetAdd = document.getElementById("upcomingSelectedAdd");

category.addEventListener("change", function () {
    if (category.value == "Attended") {
        attendedTargetAdd.style = "display: block;";
        upcomingTargetAdd.style = "display: none;";
    } else if (category.value == "Upcoming") {
        upcomingTargetAdd.style = "display: block;";
        attendedTargetAdd.style = "display: none;";
    }
})