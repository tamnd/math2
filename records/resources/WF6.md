---
records:
    - id: WF623CKR89
      kind: course-material
      title: 'Lecture 5: Transposes, permutations, spaces R^n'
      date: "2010"
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2010"
          manifestations:
            - key: m1
              kind: page
              publisher: MIT OpenCourseWare
              date: "2010"
              ids:
                ocw: 18-06-linear-algebra-spring-2010/resources/lecture-5-transposes-permutations-spaces-r-n
              access:
                class: record
      relations:
        - kind: part_of
          to: GE3WH5EF6G/e1
          source: cluster/1
      scope:
        value: deferred
        until: "2027-01-30"
        reason: the classifier score 0.993 is in the middle band
        rule: S8
        by: classify/1@2b838f8bc9d8
      catalogue:
        - source: ocw
          snapshot: blake3:ab57e74d727dbbb8cc6f30102b1562b267a6d76a54ffa725885e5e4ddfbb57b8
          native_id: 18-06-linear-algebra-spring-2010/resources/lecture-5-transposes-permutations-spaces-r-n
          level: manifestation
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
        - op: scope
          at: "2026-11-01"
          by: classify/1@2b838f8bc9d8
          note: from deferred to deferred
    - id: WF64CGYVK1
      kind: preprint
      title: Predicting properties of Scrooge ensembles with high accuracy and low sample complexity
      creators:
        - name: Yue Wu
          role: author
        - name: Yuzhi Tong
          role: author
        - name: Helen Propson
          role: author
        - name: Yihui Quek
          role: author
        - name: Liang Mao
          role: author
      date: "2026-09-30"
      subjects:
        - system: arxiv
          code: quant-ph
        - system: arxiv
          code: cond-mat.stat-mech
        - system: arxiv
          code: math-ph
        - system: arxiv
          code: math.MP
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-30"
          ids:
            arxiv: "2609.39992"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.39992"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
---
