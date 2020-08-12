using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class NewBehaviourScript : MonoBehaviour
{
     public Transform pos;
     public float speed=0.9f;
     public SpriteRenderer sprit;
     public Rigidbody2D jump;
     public float fuerzaS=8f;
     public bool puedeSaltar = false;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
        if(Input.GetKey(KeyCode.D)){
             pos.position += new Vector3(1f,0,0) * speed*Time.deltaTime;   
             sprit.flipX = false;       
        }
         
        if(Input.GetKey(KeyCode.A)){
             pos.position -= new Vector3(1f,0,0) * speed*Time.deltaTime;   
             sprit.flipX = true; 
        }
        if(Input.GetKeyDown(KeyCode.W) && puedeSaltar==true){
            jump.AddForce(Vector2.up * fuerzaS ,ForceMode2D.Impulse);
        }
    }
    public void OnCollisionEnter2D(Collision2D toque){
        if(toque.gameObject.tag == "Hurt"){
             pos.position = new Vector3(-6f,0,0);
        }
        if(toque.gameObject.tag == "suelo"){
             puedeSaltar = true; 
        }
         
    }
    
     public void OnCollisionExit2D(Collision2D toque){
        if(toque.gameObject.tag == "suelo"){
             puedeSaltar = false; 
        }
    }
}
