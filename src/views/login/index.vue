<template>
  <div class="login-container">
    <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form" autocomplete="on" label-position="left">

      <div class="title-container">
        <h1 class="title">Club Chinois Admin</h1>
      </div>
      <div class="title-container">
        <h1 class="sub-title" v-if="isLogin">Login</h1>
        <h1 class="sub-title" v-else>Register</h1>
      </div>

      <div class="input-item">
        <el-form-item prop="username">
          <span class="svg-container">
            <svg-icon icon-class="user" />
          </span>
          <el-input
            ref="username"
            v-model="loginForm.username"
            placeholder="Username"
            name="username"
            type="text"
            tabindex="1"
            autocomplete="on"
          />
        </el-form-item>
      </div>
      
      <div class="input-item">
        <el-tooltip v-model="capsTooltip" content="Caps lock is On" placement="right" manual>
          <el-form-item prop="password">
            <span class="svg-container">
              <svg-icon icon-class="password" />
            </span>
            <el-input
              :key="passwordType"
              ref="password"
              v-model="loginForm.password"
              :type="passwordType"
              placeholder="Password"
              name="password"
              tabindex="2"
              autocomplete="on"
              @keyup.native="checkCapslock"
              @blur="capsTooltip = false"
            />
            <span class="show-pwd" @click="showPwd">
              <svg-icon :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'" />
            </span>
          </el-form-item>
        </el-tooltip>
      </div>
      
      <div class="input-item" v-if='!isLogin'>
        <el-tooltip v-model="capsTooltip" content="Caps lock is On" placement="right" manual>
          <el-form-item prop="password">
            <span class="svg-container">
              <svg-icon icon-class="password" />
            </span>
            <el-input
              :key="passwordType"
              v-model="password_sec"
              :type="passwordType"
              placeholder="Enter Password Again"
              name="password"
              tabindex="2"
              autocomplete="on"
              @keyup.native="checkCapslock"
              @blur="capsTooltip = false"
            />
            <span class="show-pwd" @click="showPwd">
              <svg-icon :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'" />
            </span>
          </el-form-item>
        </el-tooltip>
      </div>

      <el-button :loading="loading" type="primary" v-if='isLogin'  style="width:100%;margin-bottom:30px;" @click.native.prevent="handleLogin">Login</el-button>
      <el-button :loading="loading" type="primary" v-else style="width:100%;margin-bottom:30px;" @click.native.prevent="handleRegister">Register</el-button>

      <div class="lr-title">
          <p v-if="!isLogin">
            Already signed up? <a @click="isLogin = (isLogin==true) ? false : true">Login</a>
          </p>
          <p v-else>
            have no account? <a @click="isLogin = (isLogin==true) ? false : true">Register</a>
          </p>
      </div>
    </el-form>

  </div>
</template>

<script>

export default {
  name: 'Login',
  data() {
    const validateUsername = (rule, value, callback) => {
      if (value.length < 0) {
        callback(new Error('Please enter the correct user name'))
      } else {
        callback()
      }
    }
    const validatePassword = (rule, value, callback) => {
      if (value.length < 6) {
        callback(new Error('The password can not be less than 6 digits'))
      } else {
        callback()
      }
    }
    const validatePassword_sec = (rule, value, callback) => {
      if (value.length < 6) {
        callback(new Error('The password can not be less than 6 digits'))
      } else {
        callback()
      }
    }
    return {
      loginForm: {
        username: '',
        password: '',
      },
      password_sec: '',
      loginRules: {
        username: [{ required: true, trigger: 'blur', validator: validateUsername }],
        password: [{ required: true, trigger: 'blur', validator: validatePassword }],
        password_sec: [{ required: true, trigger: 'blur', validator: validatePassword_sec }],        
      },
      isLogin: true,
      passwordType: 'password',
      capsTooltip: false,
      loading: false,
      showDialog: false,
      redirect: undefined,
    }
  },
  watch: {

  },
  created() {
    // window.addEventListener('storage', this.afterQRScan)
  },
  mounted() {
    if (this.loginForm.username === '') {
      this.$refs.username.focus()
    } else if (this.loginForm.password === '') {
      this.$refs.password.focus()
    }
  },
  destroyed() {
    // window.removeEventListener('storage', this.afterQRScan)
  },
  methods: {
    checkCapslock(e) {
      const { key } = e
      this.capsTooltip = key && key.length === 1 && (key >= 'A' && key <= 'Z')
    },
    showPwd() {
      if (this.passwordType === 'password') {
        this.passwordType = ''
      } else {
        this.passwordType = 'password'
      }
      this.$nextTick(() => {
        this.$refs.password.focus()
      })
    },

    async handleRegister() {
      this.$refs.loginForm.validate(async(valid) => {
        if (valid && this.password_sec==this.loginForm.password) {
          this.loading = true    
          let payload = {'password': this.loginForm.password, 'username': this.loginForm.username}
          this.$store.dispatch('user/register', payload)
            .then(async(res) => {
              location.reload()
              this.loading = false
            })
            .catch((e) => {
              this.loginForm.username = ''; this.loginForm.password = ''; this.password_sec = '';
              console.error('errors in Page jumping\n', e)
              this.loading = false
            })
          
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },

    async handleLogin() {
      this.$refs.loginForm.validate(async(valid) => {
        if (valid) {
          this.loading = true    
          let payload = {'password': this.loginForm.password, 'username': this.loginForm.username}
          // const promise = new Promise((resolve, reject) => {
          //   this.$store.dispatch('user/login', payload)
          // });
          this.$store.dispatch('user/login', payload)
            .then(async() => {
              // this.$router.push({ path: this.redirect || '/' })
              // console.log('Roles in Getters:',  this.$store.getters.roles)
              this.$router.push({path:'/dashboard'})
              this.$message({
                message: 'Login successfully!!!',
                type: 'success'
              });
              this.loading = false
            })
            .catch((e) => {
              console.error('errors in Page jumping\n', e)
              this.loading = false
            })
            if (this.$store.getters.cas_id==undefined || this.$store.getters.cas_id==0) {
              setTimeout(() => {
                console.log('This cas_id in Store is undefined now....: ', this.$store.getters.cas_id)
                this.getUserInfo()
              }, 5000);
            } else {
              this.getUserInfo()
              console.log('cas_id in Store: ', this.$store.getters.cas_id)
            }
            
          
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },

    async getUserInfo() {
      await this.$store.dispatch('user/getRole', this.$store.getters.cas_id)
      .then(res => {
        const data = res
        // console.log('UserInfo in getUserInfo() in login/index.vue:', data)
        return data
      }).catch((e) => {
        console.error(e)
      })
    }
  }
}
</script>

<style lang="scss">
/* 修复input 背景不协调 和光标变色 */
/* Detail see https://github.com/PanJiaChen/vue-element-admin/pull/927 */

$bg:#283443;
$light_gray:#fff;
$cursor: #fff;

@supports (-webkit-mask: none) and (not (cater-color: $cursor)) {
  .login-container .el-input input {
    color: $cursor;
  }
}

/* reset element-ui css */
.login-container {
  .el-input {
    display: inline-block;
    height: 47px;
    width: 85%;

    input {
      background: transparent;
      border: 0px;
      -webkit-appearance: none;
      border-radius: 0px;
      padding: 12px 5px 12px 15px;
      color: $light_gray;
      height: 47px;
      caret-color: $cursor;

      &:-webkit-autofill {
        box-shadow: 0 0 0px 1000px $bg inset !important;
        -webkit-text-fill-color: $cursor !important;
      }
    }
  }

  .el-form-item {
    border: 1px solid rgba(255, 255, 255, 0.1);
    background: rgba(0, 0, 0, 0.1);
    border-radius: 5px;
    color: #454545;
  }
}
</style>

<style lang="scss" scoped>
$bg:#2d3a4b;
$dark_gray:#889aa4;
$light_gray:#eee;

.login-container {
  min-height: 100%;
  width: 100%;
  background-color: $bg;
  overflow: hidden;
  .input-item {
    display: flex;
    flex-direction: column;
  }
  .tooltip-txt {
    color: rgb(202, 197, 197);
    font-weight: bolder;
    margin: 0vw 0vw 0.2vw 0.4vw;
    display: flex;
    justify-content: start;
  }
  .login-form {
    position: relative;
    width: 520px;
    max-width: 100%;
    padding: 160px 35px 0;
    margin: 0 auto;
    overflow: hidden;
  }

  .tips {
    font-size: 14px;
    color: #fff;
    margin-bottom: 10px;

    span {
      &:first-of-type {
        margin-right: 16px;
      }
    }
  }

  .svg-container {
    padding: 6px 5px 6px 15px;
    color: $dark_gray;
    vertical-align: middle;
    width: 30px;
    display: inline-block;
  }

  .title-container {
    position: relative;

    .title {
      font-size: 26px;
      color: $light_gray;
      margin: 0px auto 40px auto;
      text-align: center;
      font-weight: bold;
    }
    .sub-title {
      font-size: 20px;
      color: $light_gray;
    }
  }


  .show-pwd {
    position: absolute;
    right: 10px;
    top: 7px;
    font-size: 16px;
    color: $dark_gray;
    cursor: pointer;
    user-select: none;
  }

  .thirdparty-button {
    position: absolute;
    right: 0;
    bottom: 6px;
  }

  .lr-title{
    position: relative;
    height:32px;
    line-height: 2px;
    margin-bottom: 20px;
    display: flex;
    justify-content: flex-end;
  }
  .lr-title p{
      font-size: 10px;
      color:rgb(219, 219, 183);
      font-weight: bold;
      /*width:50%;*/
  }

  @media only screen and (max-width: 470px) {
    .thirdparty-button {
      display: none;
    }
  }
}
</style>
