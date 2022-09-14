from borb.io.read.types import Decimal as bDecimal
from borb.io.read.types import String
from borb.io.read.types import Stream
from borb.io.read.types import Dictionary
from borb.io.read.types import List
from borb.pdf import Document


def add_document_level_javascript(doc: Document):
    # build global_js_stream
    global_js_stream = Stream()
    global_js_stream[Name("Type")] = Name("JavaScript")
    global_js_stream[
        Name("DecodedBytes")
    ] = b"""
var state = 'START';
var arg1 = 0;
var arg2 = 0;
var disp = '';
var oper = '';

function to_string(f){
	if(f > 99999999){ return '99999999'; }
	if(f < -99999999){ return '-99999999'; }
	x = f.toString();
  if(x.length > 8){ x = x.substring(0, 8);}
	return x;	
}

function is_number(token){
	return token == '0' || token == '1' || token == '2' || token == '3' || token == '4' || token == '5' || token == '6' || token == '7'  || token == '8' || token == '9';
}

function is_binary_operator(token){
	return token == '+' || token == '-' || token == 'x' || token == '/';
}

function apply_operator(a1, a2, o){
	if(o == '+'){ return a1 + a2; }
	if(o == '-'){ return a1 - a2; }
	if(o == 'x'){ return a1 * a2; }
	if(o == '/'){ 
		if(a2 == 0){
			return 0;
		}
		return a1 / a2; 
	}
}

function process_token(token){
	if(token == 'AC'){
		state = 'START';
		arg1 = 0;
		arg2 = 0;
		disp = '';
		oper = '';
    this.getField("field-000").value = disp;
		return;
	}
	if(state == 'START'){
		if(token == '.'){
			disp = '0.';
      this.getField("field-000").value = disp;
			state = 'ARG1_FLOAT';
			return;
		}
		if(is_number(token)){
			disp = token;
      this.getField("field-000").value = disp;
			state = 'ARG1'
			return;
		}
	}
	/* 
	 * ARG1
	 * arg1 is being built
	 */
	if(state == 'ARG1'){
		if(token == '.'){
			disp += '.';
      this.getField("field-000").value = disp;
			state = 'ARG1_FLOAT';
			return;
		}
		if(is_number(token)){
			disp += token;
      this.getField("field-000").value = disp;
			return;
		}
		if(is_binary_operator(token)){
			arg1 = parseFloat(disp);
			disp = '';
      this.getField("field-000").value = disp;
			oper = token;
			state = 'OPERATOR'
			return;
		}
	}
	/* 
	 * ARG1_FLOAT
	 * arg1 is being built, and a decimal point has been entered
	 */
	if(state == 'ARG1_FLOAT'){
		if(is_number(token)){
			disp += token;
      this.getField("field-000").value = disp;
			return;
		}
		if(is_binary_operator(token)){
			arg1 = parseFloat(disp);
			disp = '';
      this.getField("field-000").value = disp;
			oper = token;
			state = 'OPERATOR'
			return;
		}
	}
	/* 
	 * BINARY_OPERATOR
	 * a binary operator was entered
	 */
	if(state == 'OPERATOR'){
		if(token == '.'){
			disp = '0.';
      this.getField("field-000").value = disp;
			state = 'ARG2_FLOAT';
			return;
		}
		if(is_number(token)){
			disp = token;
      this.getField("field-000").value = disp;
			state = 'ARG2'
			return;
		}
	}
	/* 
	 * ARG2
	 * arg2 is being built
	 */
	if(state == 'ARG2'){
		if(token == '.'){
			disp += '.';
      this.getField("field-000").value = disp;
			state = 'ARG2_FLOAT';
			return;
		}
		if(is_number(token)){
			disp += token;
      this.getField("field-000").value = disp;
			return;
		}
		if(is_binary_operator(token)){
			arg1 = apply_operator(arg1, parseFloat(disp), oper);
			disp = to_string(arg1);
      this.getField("field-000").value = disp;
			oper = token;
			state = 'OPERATOR'
			return;
		}
		if(token == '='){
			arg2 = parseFloat(disp);
			disp = to_string(apply_operator(arg1, arg2, oper));
      this.getField("field-000").value = disp;
			state = 'EQUALS';
			return;
		}
	}
	if(state == 'ARG2_FLOAT'){
		if(is_number(token)){
			disp += token;
      this.getField("field-000").value = disp;
			return;
		}
		if(is_binary_operator(token)){
			arg1 = apply_operator(arg1, parseFloat(disp), oper);
			disp = to_string(arg1);
      this.getField("field-000").value = disp;
			oper = token;
			state = 'OPERATOR'
			return;
		}
		if(token == '='){
			arg2 = parseFloat(disp);
			disp = to_string(apply_operator(arg1, arg2, oper));
      this.getField("field-000").value = disp;
			state = 'EQUALS';
			return;
		}
	}	
	if(state == 'EQUALS'){
		if(token == '='){
			disp = to_string(apply_operator(parseFloat(disp), arg2, oper));
      this.getField("field-000").value = disp;
			return;
		}
		if(token == '.'){
			disp = '0.';
      this.getField("field-000").value = disp;
			state = 'ARG1_FLOAT';
			return;
		}
		if(is_number(token)){
			disp = token;
      this.getField("field-000").value = disp;
			state = 'ARG1';
			return;
		}
		if(is_binary_operator(token)){
			arg1 = parseFloat(disp);
			oper = token;
			state = 'OPERATOR';
			return;
		}
	}
}
this.getField("field-000").fillColor = color.transparent;
this.getField("field-000").textFont = "Courier";
app.runtimeHighlightColor = ["RGB", 47/255, 53/255, 51/255];
"""

    global_js_stream[Name("Filter")] = Name("FlateDecode")

    # build global js dictionary
    global_js_dictionary = Dictionary()
    global_js_dictionary[Name("S")] = Name("JavaScript")
    global_js_dictionary[Name("JS")] = global_js_stream

    # build name tree
    root = doc["XRef"]["Trailer"]["Root"]
    root[Name("Names")] = Dictionary()
    names = root["Names"]
    names[Name("JavaScript")] = Dictionary()
    names["JavaScript"][Name("Kids")] = List()

    # build leaf
    kids_01 = Dictionary()
    kids_01[Name("Limits")] = List()
    kids_01["Limits"].append(String("js-000"))
    kids_01["Limits"].append(String("js-000"))
    kids_01[Name("Names")] = List()
    kids_01["Names"].append(String("js-000"))
    kids_01["Names"].append(global_js_dictionary)

    names["JavaScript"]["Kids"].append(kids_01)
