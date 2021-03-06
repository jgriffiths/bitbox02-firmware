// Copyright 2020 Shift Crypto AG
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

//! Stubs for testing.

pub use super::types::{ConfirmParams, Font};

use crate::password::Password;

use core::marker::PhantomData;

pub struct Component<'a> {
    is_pushed: bool,
    _p: PhantomData<&'a ()>,
}

impl<'a> Component<'a> {
    pub fn screen_stack_push(&mut self) {
        if self.is_pushed {
            panic!("component pushed twice");
        }
        self.is_pushed = true;
    }
}

impl<'a> Drop for Component<'a> {
    fn drop(&mut self) {
        if !self.is_pushed {
            panic!("component not pushed");
        }
    }
}

pub fn trinary_input_string_create_password<'a, F>(
    _title: &str,
    _special_chars: bool,
    _confirm_callback: F,
) -> Component<'a>
where
    F: FnMut(Password) + 'a,
{
    panic!("not implemented")
}

pub fn confirm_create<'a, F>(_params: &ConfirmParams, _result_callback: F) -> Component<'a>
where
    F: FnMut(bool) + 'a,
{
    panic!("not implemented")
}

pub fn screen_process() {}

pub fn status_create<'a, F>(_text: &str, _status_success: bool, _callback: F) -> Component<'a>
where
    F: FnMut() + 'a,
{
    panic!("not implemented")
}

pub fn with_lock_animation<F: Fn()>(_f: F) {
    panic!("not implemented")
}

pub fn screen_stack_pop_all() {
    panic!("not implemented")
}
