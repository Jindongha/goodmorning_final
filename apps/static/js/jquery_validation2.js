$("#mkd").validate({

	rules: { //규칙 부분

		col: {

				required: true, // 두 가지 규칙 이상 추가 시.
				minlength: 1 // 최소 길이 2 이상
				''' 숫자만 쓸 수 있게 / 6 이상은 fail'''

			},

			row: {

				required: true,
				minlength: 1

			},


	},

	messages: { // 유효성 검사에서 부적합함이 적발된 경우

		col: {

			required: "Please enter a number between 1 to 5", // 규칙이 여러개일 땐, 각 규칙에 대응해서 메시지를 띄워줍니다.
			minlength: "You should write only one number"

		},

		row: {

			required: "Please enter a number between 1 to 5", // 규칙이 여러개일 땐, 각 규칙에 대응해서 메시지를 띄워줍니다.
			minlength: "You should write only one number"

		},

});
