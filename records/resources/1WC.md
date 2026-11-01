---
records:
    - id: 1WC7R4BJF8
      kind: monograph
      title: A Classical Invitation to Algebraic Numbers and Class Fields
      creators:
        - name: Harvey Cohn
          role: author
      date: "1978"
      msc:
        - code: 11-XX
          from: classify/1@2b838f8bc9d8
      expressions:
        - key: e1
          kind: edition
          date: "1978"
          ids:
            doi: 10.1007/978-1-4612-9950-9
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1978"
              ids:
                isbn:
                    - "9780387903453"
                    - "9781461299509"
              access:
                class: record
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-9950-9
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: 1WCXV5PVZA
      kind: preprint
      title: Descending finite projective modules from a Novikov ring
      creators:
        - name: Dongryul Kim
          role: author
      date: "2024-02-27"
      msc:
        - code: 13-XX
          from: arxiv
        - code: 14-XX
          from: arxiv
      subjects:
        - system: arxiv
          code: math.AC
        - system: arxiv
          code: math.AG
      expressions:
        - key: e1
          kind: version
          label: preprint
          language: en
          date: "2024-02-27"
          ids:
            arxiv: "2402.17852"
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2402.17852"
          level: work
        - source: arxiv_text
          snapshot: blake3:b523016991566b44cacf0976b2dcb4dfca52ceb7fd07e311b05971173c8f0b4d
          native_id: "2402.17852"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
