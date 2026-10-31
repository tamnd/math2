---
records:
    - id: QPB0SH99WD
      kind: monograph
      title: 'Lectures on Polytopes: Updated Seventh Printing of the First Edition'
      creators:
        - name: Günter M. Ziegler
          role: author
          ids:
            orcid: 0000-0003-1502-1915
      date: "1995"
      msc:
        - code: 52-01
          from: zbmath_search
        - code: 52A20
          from: zbmath_search
        - code: 52Bxx
          from: zbmath_search
        - code: 05B35
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          label: 1st edition
          language: en
          date: "1995"
          ids:
            doi: 10.1007/978-1-4613-8431-1
            zbl: "0823.52002"
            zbl_id: "722614"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1995"
              ids:
                isbn:
                    - "9780387943657"
                    - "9781461384311"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4613-8431-1
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "722614"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: QPBQR3SJNA
      kind: course
      title: Complex Analysis
      creators:
        - name: A. Swaminathan
          role: instructor
        - name: V. K. Katiyar
          role: instructor
      ids:
        course: 00582g326:111107056
      expressions:
        - key: e1
          kind: edition
          language: en
          manifestations:
            - key: m1
              kind: page
              publisher: IIT Roorkee
              ids:
                nptel: "111107056"
              access:
                class: record
      scope:
        value: in
        rule: S6
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111107056"
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
          at: "2026-10-31"
          by: m2 v0.6.4 scope/1
          note: from deferred to in
---
