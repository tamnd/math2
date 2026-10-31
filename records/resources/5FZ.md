---
records:
    - id: 5FZGDECW2R
      kind: preprint
      title: Genus, Morse Index, and Area of Minimal Surfaces in Three-Manifolds
      creators:
        - name: Riccardo Caniato
          role: author
      date: "2026-09-25"
      subjects:
        - system: arxiv
          code: math.DG
        - system: arxiv
          code: math.AP
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-25"
          ids:
            arxiv: "2609.32001"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.32001"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
    - id: 5FZPZ7R15G
      kind: monograph
      title: 'Lectures on Probability Theory and Statistics: Ecole d’Eté de Probabilités de Saint-Flour XXX - 2000'
      creators:
        - name: Sergio Albeverio
          role: editor
        - name: Walter Schachermayer
          role: editor
        - name: Michel Talagrand
          role: editor
        - name: Pierre Bernard
          role: editor
      date: "2003"
      expressions:
        - key: e1
          kind: edition
          date: "2003"
          ids:
            doi: 10.1007/3-540-44922-1
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2003"
              ids:
                isbn:
                    - "9783540403357"
                    - "9783540449225"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/3-540-44922-1
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
