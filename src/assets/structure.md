## Features
- Login / Logout

- Permission Authentication
  - Page permission
  - Directive permission
  - Permission configuration page
  - Two-step login

- Multi-environment build
  - dev sit stage prod

- Global Features
  - I18n
  - Multiple dynamic themes
  - Dynamic sidebar (supports multi-level routing)
  - Dynamic breadcrumb
  - Tags-view (Tab page Support right-click operation)
  - Svg Sprite
  - Mock data
  - Screenfull
  - Responsive Sidebar

- Editor
  - Rich Text Editor
  - Markdown Editor
  - JSON Editor

- Excel
  - Export Excel
  - Upload Excel
  - Visualization Excel
  - Export zip

- Table
  - Dynamic Table
  - Drag And Drop Table
  - Inline Edit Table

- Error Page
  - 401
  - 404

- Components
  - Avatar Upload
  - Back To Top
  - Drag Dialog
  - Drag Select
  - Drag Kanban
  - Drag List
  - SplitPane
  - Dropzone
  - Sticky
  - CountTo

- Advanced Example
- Error Log
- Dashboard
- Guide Page
- ECharts
- Clipboard
- Markdown to html


## Project Structure

├── build                      # build config files
├── mock                       # mock data
├── public                     # pure static assets (directly copied)
│   │── favicon.ico            # favicon
│   └── index.html             # index.html template
├── src                        # main source code
│   ├── api                    # api service (Encapsulation of axios)
│   ├── assets                 # module assets like fonts,images (processed by webpack)
│   |   ├── css                  # css
│   |   ├── img                  # img
│   |   ├── svg                  # svg 
│   ├── components             # global components
│   ├── layout                 # global layout
│   ├── plugins
│   │   ├── directive              # global directive
│   │   ├── filters                # global filter
│   │   ├── filters                # global filter
│   ├── router                 # router
│   ├── store                  # store
│   ├── styles                 # global css
│   ├── utils                  # global utils
│   ├── vendor                 # vendor
│   ├── views                  # views
│   ├── App.vue                # main app component
│   ├── main.js                # app entry file
│   └── permission.js          # permission authentication
├── tests                      # tests
├── .env.xxx                   # env variable configuration
├── .eslintrc.js               # eslint config
├── .babelrc                   # babel config
├── .travis.yml                # automated CI configuration
├── vue.config.js              # vue-cli config
├── postcss.config.js          # postcss config
└── package.json               # package.json