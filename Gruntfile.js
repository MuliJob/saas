module.exports = function(grunt) {
  grunt.initConfig({
    sass: {
      dist: {
        options: {
          implementation: require('sass'),
          style: 'compressed'
        },
        files: {
          'media/assets/styles/main.css': 'media/assets/styles/main.scss' 
        }
      }
    },
    watch: {
      sass: {
        files: ['media/assets/styles/*.scss'],
        tasks: ['sass:dist']
      }
    }
  });

  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask('default', ['sass:dist']);
};
