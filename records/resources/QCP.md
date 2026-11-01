---
records:
    - id: QCPRPB65R6
      kind: problem-set
      title: Kvant 1994, no. 6
      creators:
        - name: Kvant editorial board
          role: editor
      date: "1994"
      msc:
        - code: 00A07
          from: kvant
        - code: 97U40
          from: kvant
      expressions:
        - key: e1
          kind: edition
          language: ru
          date: "1994"
          structure: QCPRPB65R6/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 1994-6
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
    - id: QCPX7AB0QY
      kind: monograph
      title: Theorems and Counterexamples in Mathematics
      creators:
        - name: Bernard R. Gelbaum
          role: author
        - name: John M. H. Olmsted
          role: author
      date: "1990"
      msc:
        - code: 00A07
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1990"
          ids:
            doi: 10.1007/978-1-4612-0993-5
            zbl: "0702.00005"
            zbl_id: "46568"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1990"
              ids:
                isbn:
                    - "9781461269755"
                    - "9781461209935"
              access:
                class: record
      relations:
        - kind: part_of
          to: AQAR17SPHM
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-0993-5
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "46568"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
---
