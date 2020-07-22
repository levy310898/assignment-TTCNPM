var root = document.getElementById("root");

$(document).ready(function(){
    $("#addQuestion").click(function(e){
        e.preventDefault();
        $("#noElement").remove();
        console.log("hello from newTest i'm addQuestion");
        // root.innerHTML += createQuestion();
        $("#root").append(createQuestion());
    });
})

function addQuestionInRoot(element){
    root.innerHTML += element;
}

$(document).on('click','.deleteQuestion',function(e){
    e.preventDefault();
    let parent = $(this).parent();
    $(parent).remove();
    return false;
})

function createQuestion(){
    let ques = `
        <div class = "ques-box">
            <div class="form-group row">
                <label class="col-lg-2 col-md-0">Nhập câu hỏi: </label>
                <input type="text" name="question" id="" class="form-control col-lg-10 col-md-12" placeholder="Nhập câu hỏi: ">
            </div>
            <div class="form-group row">
                <label class="col-lg-2 col-md-0">Nhập câu trả lời A: </label>
                <input type="text" name="answerA" id="" class="form-control col-lg-10 col-md-12" placeholder="Nhập câu trả lời thứ nhất: ">
            </div>
            <div class="form-group row">
                <label class="col-lg-2 col-md-0">Nhập câu trả lời B: </label>
                <input type="text" name="answerB" id="" class="form-control col-lg-10 col-md-12" placeholder="Nhập câu trả lời thứ hai: ">
            </div>
            <div class="form-group row">
                <label class="col-lg-2 col-md-0">Nhập câu trả lời C: </label>
                <input type="text" name="answerC" id="" class="form-control col-lg-10 col-md-12" placeholder="Nhập câu trả lời thứ ba: ">
            </div>
            <div class="form-group row">
                <label class="col-lg-2 col-md-0">Nhập câu trả lời D: </label>
                <input type="text" name="answerD" id="" class="form-control col-lg-10 col-md-12" placeholder="Nhập câu trả lời thứ tư: ">
            </div>

            <div class="form-group"> 
                <label for="sel1">Chọn đáp án đúng cho câu hỏi:</label>
                <select class="form-control" name = "answer" id="sel1">
                    <option value = "A">A</option>
                    <option value = "B">B</option>
                    <option value = "C">C</option>
                    <option value = "D">D</option>
                </select>
            </div>
            <span class = "deleteQuestion" ><i class="fas fa-times"></i></span>
        </div>
    `;

    return ques;
}