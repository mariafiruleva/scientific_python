import re

config = dict (
paths = {
'cond1' : "reads/A.fq.gz" ,
'input' : "reads/B.fq.gz"
} ,
mem_gb = dict ( cond1 = 10 )
)
@workflow.rule(name='all', lineno=10, snakefile='/home/marina/snakemake_tutorial/examples/example_03/example_03.4.smk')

@workflow.input( "bams/cond1.bam"
)


@workflow.norun()
@workflow.run
def __rule_all(input, output, params, wildcards, threads, resources, log, version, rule, conda_env, container_img, singularity_args, use_singularity, env_modules, bench_record, jobid, is_shell, bench_iteration, cleanup_scripts, shadow_dir, edit_notebook):
	pass
def align_input_function ( wildcards ) :
				paths = config [ 'paths' ]

				sample_path = paths [ wildcards . sample ]
				if 'input' in paths :
								return dict ( fq = sample_path , input = paths [ 'input' ] )
				else :
								return [ sample_path ]


@workflow.rule(name='align', lineno=30, snakefile='/home/marina/snakemake_tutorial/examples/example_03/example_03.4.smk')

@workflow.input( unpack ( align_input_function )
)

@workflow.output( "bams/{sample}.bam"
)

@workflow.threads( 10
)

@workflow.params(
						mem = lambda wildcards , threads : f'{(threads * config["mem_gb"][f"{wildcards.sample}"])}gb' ,
						basename = lambda wildcards , output : re . sub ( '\..*' , '' , str ( output ) )
)
@workflow.run
def __rule_align(input, output, params, wildcards, threads, resources, log, version, rule, conda_env, container_img, singularity_args, use_singularity, env_modules, bench_record, jobid, is_shell, bench_iteration, cleanup_scripts, shadow_dir, edit_notebook):
				if not input . get ( 'input' ) :
								shell ( 'echo "tool {input} {params.basename}" > {output}' )
				else :
								shell ( 'echo "tool --input {input.input} {input.fq} {params.mem}" > {output}' )



