var rgbLedMatrix = angular.module('rgbLedMatrix',[]);

function MatrixCtrl($scope,$http) {

    // Color Pallete
    $scope.colors = [
        {color:"grey",      dec:0},  // Pixel is OFF
        {color:"red",       dec:224},
        {color:"orange",    dec:252},
        {color:"yellow",    dec:124},
        {color:"green",     dec:28},
        {color:"teal",      dec:31},
        {color:"blue",      dec:3},
        {color:"magenta",   dec:227},
        {color:"purple",    dec:66},
        {color:"white",     dec:255}
    ];

    $scope.selected = $scope.colors[0];

    // Populate pixels array with OFF pixels
    $scope.pixels = Array(64);
    for (var i=0;i<$scope.pixels.length;++i) {
        $scope.pixels[i] = {color: $scope.colors[0].color, dec:0, state: false};
    }

    // Light the pixel on and post data to server
    $scope.putPixel = function(pixel) {
        // grey means pixel OFF
        pixel.state = !($scope.selected.color === 'grey')
        pixel.color = $scope.selected.color;
        pixel.dec = $scope.selected.dec;

        // Generate array of color values
        var colors = [pixel.dec for each(pixel in $scope.pixels)]
        $http.post("/test",{pixels:uneval(colors)})
    };

    // Change current selected color
    $scope.setColor = function(colorBox){
        $scope.selected = colorBox;
    }
}