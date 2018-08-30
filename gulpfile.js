var gulp = require('gulp')
var sass = require('gulp-sass')
var postcss = require('gulp-postcss')
var autoprefixer = require('autoprefixer')
let cleanCSS = require('gulp-clean-css');


var scssSrc = [
 './static/**/*.scss',
 './apps/**/*.scss',
]

var postcssPlugins = [
  autoprefixer()
]

gulp.task('sass', () => {
  return gulp.src(scssSrc, {base: './'})
    .pipe(sass().on('error', sass.logError))
    .pipe(postcss(postcssPlugins))
    .pipe(cleanCSS({compatibility: 'ie9'}))
    .pipe(gulp.dest('.'))
})

gulp.task('sass:watch', function () {
  gulp.watch('./**/*.scss', ['sass']);
})
