---
records:
    - id: NM6X0BEQR9
      kind: monograph
      title: Toposes, Algebraic Geometry and Logic
      creators:
        - name: I. Bucur
          role: author
        - name: J. Giraud
          role: author
        - name: N. Goodman
          role: author
        - name: J. Myhill
          role: author
        - name: L. Illusie
          role: author
        - name: J. Lambek
          role: author
        - name: D. S. Scott
          role: author
        - name: M. Tierney
          role: author
        - name: F. W. Lawvere
          role: editor
      date: "1972"
      expressions:
        - key: e1
          kind: edition
          date: "1972"
          ids:
            doi: 10.1007/bfb0073961
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1972"
              ids:
                isbn:
                    - "9783540059202"
                    - "9783540376095"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0073961
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: NM6Z2R61CN
      kind: preprint
      title: 'On Inherent Privacy of Posterior Sampling: A Unified R\''enyi-Divergence Framework'
      creators:
        - name: Ruyu Zhou
          role: author
        - name: Fang Liu
          role: author
      date: "2026-10-14"
      subjects:
        - system: arxiv
          code: stat.ML
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: math.ST
        - system: arxiv
          code: stat.TH
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-14"
          ids:
            arxiv: "2610.19573"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.19573"
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
