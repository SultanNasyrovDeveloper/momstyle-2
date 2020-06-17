        var inputLeft = document.getElementById("left_price");
        var inputRight = document.getElementById("right_price");

        var thumbLeft = document.querySelector(".slider > .thumb.left");
        var thumbRight = document.querySelector(".slider > .thumb.right");
        var range = document.querySelector(".slider > .range");

        function setLeftValue() {
            var _this = inputLeft,
                min = parseInt(_this.min),
                max = parseInt(_this.max);

            _this.value = Math.min(parseInt(_this.value), parseInt(inputRight.value) - 1);

            var percent = ((_this.value - min) / (max - min)) * 100;

            thumbLeft.style.left = percent + "%";
            range.style.left = percent + "%";
            $('#id_price_0').val(_this.value);
        }
        setLeftValue();

        function setRightValue() {
            var _this = inputRight,
                min = parseInt(_this.min),
                max = parseInt(_this.max);

            _this.value = Math.max(parseInt(_this.value), parseInt(inputLeft.value) + 1);

            var percent = ((_this.value - min) / (max - min)) * 100;

            thumbRight.style.right = (100 - percent) + "%";
            range.style.right = (100 - percent) + "%";
            $('#id_price_1').val(_this.value)
        }
        setRightValue();

        inputLeft.addEventListener("input", setLeftValue);
        inputRight.addEventListener("input", setRightValue);

        inputLeft.addEventListener("mouseover", function() {
            thumbLeft.classList.add("hover");
        });
        inputLeft.addEventListener("mouseout", function() {
            thumbLeft.classList.remove("hover");
        });
        inputLeft.addEventListener("mousedown", function() {
            thumbLeft.classList.add("active");
        });
        inputLeft.addEventListener("mouseup", function() {
            thumbLeft.classList.remove("active");
        });

        inputRight.addEventListener("mouseover", function() {
            thumbRight.classList.add("hover");
        });
        inputRight.addEventListener("mouseout", function() {
            thumbRight.classList.remove("hover");
        });
        inputRight.addEventListener("mousedown", function() {
            thumbRight.classList.add("active");
        });
        inputRight.addEventListener("mouseup", function() {
            thumbRight.classList.remove("active");
        });